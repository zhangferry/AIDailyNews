import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';
import test from 'node:test';
import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import matter from 'gray-matter';
import newsLayout from '../../src/plugins/news-layout.mjs';

const corpusDirectory = new URL('../../src/content/blog/', import.meta.url);
const textContent = node => node.value ?? (node.children ?? []).map(textContent).join('');

function visit(node, callback) {
  callback(node);
  for (const child of node.children ?? []) visit(child, callback);
}

function snapshot(tree) {
  const externalLinks = [];
  const images = [];
  visit(tree, node => {
    const href = node.properties?.href;
    if (node.tagName === 'a' && typeof href === 'string' && /^(?:https?:)?\/\//i.test(href)) {
      externalLinks.push(href);
    }
    if (node.tagName === 'img') images.push(node.properties?.src);
  });
  return {
    // Splitting one Markdown paragraph into several blocks can move whitespace.
    text: textContent(tree).replace(/\s/g, ''),
    externalLinks,
    images,
  };
}

test('all published Markdown preserves text, external links and images after news layout', async context => {
  const filenames = (await readdir(corpusDirectory)).filter(name => name.endsWith('.md')).sort();
  assert.ok(filenames.length > 0, 'the published corpus must not be empty');
  let currentFile;
  let externalLinkCount = 0;
  let imageCount = 0;
  let metadataCount = 0;
  const transform = newsLayout();
  const processor = await createMarkdownProcessor({
    rehypePlugins: [() => tree => {
      const before = snapshot(tree);
      transform(tree);
      assert.deepEqual(snapshot(tree), before, `${currentFile}: content changed during layout`);
      externalLinkCount += before.externalLinks.length;
      imageCount += before.images.length;
      visit(tree, node => {
        if (!node.properties?.className?.includes('news-meta')) return;
        metadataCount += 1;
        const metadata = textContent(node).trim();
        assert.match(metadata, /^(?:来源|发布时间)[：:]/, `${currentFile}: unexpected metadata`);
        assert.equal(metadata.split(/\r?\n/).length, 1,
          `${currentFile}: metadata contains a multiline body summary: ${metadata}`);
      });
    }],
  });

  for (const filename of filenames) {
    currentFile = filename;
    const { content } = matter(await readFile(new URL(filename, corpusDirectory), 'utf8'));
    await processor.render(content);
  }
  context.diagnostic(`Verified ${filenames.length} reports, ${externalLinkCount} external links, ${imageCount} images and ${metadataCount} metadata paragraphs.`);
});
