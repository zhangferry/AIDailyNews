import assert from 'node:assert/strict';
import test from 'node:test';
import newsLayout from '../../src/plugins/news-layout.mjs';
const text = value => ({ type: 'text', value });
const el = (tagName, children = [], properties = {}) => ({ type: 'element', tagName, properties, children });
const flatten = node => node.value ?? (node.children ?? []).map(flatten).join('');
const find = (node, tag) => [node, ...(node.children ?? []).flatMap(n => find(n, tag))].filter(n => n.tagName === tag);

test('legacy metadata, image, summary and list survive grouping with stable heading ids', () => {
  const summary = el('strong', [text('完整摘要')]);
  const image = el('img', [], { src: 'https://example.com/photo.png', alt: '' });
  const root = { type: 'root', children: [
    el('blockquote', [el('ul', [el('li', [text('文章标题')])])]),
    el('h2', [text('Tech News')], { id: 'tech-news' }),
    el('h3', [el('a', [text('文章标题')], { href: 'https://example.com' })], { id: 'article' }),
    el('p', [text('来源：Example')]),
    el('p', [text('发布时间：2026-10-25 08:00:00\n'), image, text('\n'), summary]),
    el('ul', [el('li', [text('第一条要点')])]),
  ] };
  const original = flatten(root).replace(/\s/g, '');
  newsLayout()(root);
  assert.equal(flatten(root).replace(/\s/g, ''), original);
  assert.equal(find(root, 'section').length, 1);
  assert.equal(find(root, 'h3')[0].properties.id, 'article');
  assert.equal(find(root, 'img')[0].properties.loading, 'lazy');
  assert.equal(find(root, 'img')[0].properties.alt, '文章标题');
  assert.equal(find(root, 'a')[0].properties.href, '#article');
  assert.ok(find(root, 'p').some(p => p.children.includes(summary) && !p.children.includes(image)));
  assert.ok(find(root, 'p').some(p => p.children.includes(image) && !flatten(p).includes('发布时间')));
});

test('ordinary pages and older reports without images preserve their content', () => {
  const root = { type: 'root', children: [el('h2', [text('关于本站')]), el('p', [text('介绍文字')])] };
  const original = structuredClone(root);
  newsLayout()(root);
  assert.deepEqual(root, original);
  const report = { type: 'root', children: [el('h3', [text('旧文章')], { id: 'old' }), el('p', [text('来源：RSS')]), el('p', [text('发布时间：2024-02-01')]), el('p', [text('旧版普通摘要')])] };
  const content = flatten(report);
  newsLayout()(report);
  assert.equal(flatten(report), content);
  assert.equal(find(report, 'section').length, 1);
});

test('multiple categories retain heading order and internal/external links', () => {
  const root = { type: 'root', children: ['一', '二'].flatMap((name, i) => [el('h2', [text(name)]), el('h3', [el('a', [text(name)], { href: `https://example.com/${i}` })], { id: name }), el('p', [text('来源：RSS')]), el('p', [text('内容')])]) };
  newsLayout()(root);
  assert.equal(find(root, 'section').length, 2);
  assert.deepEqual(find(root, 'h2').map(flatten), ['一', '二']);
  assert.deepEqual(find(root, 'a').map(n => n.properties.href), ['https://example.com/0', 'https://example.com/1']);
});

test('plain historical summary after timestamp remains body text', () => {
  const root = { type: 'root', children: [el('h3', [text('旧文')]), el('p', [text('来源：RSS')]), el('p', [text('发布时间：2026-04-12 17:51:00\n这里是完整的普通文本摘要。')])] };
  newsLayout()(root);
  const paragraphs = find(root, 'p');
  const summary = paragraphs.find(p => flatten(p).includes('普通文本摘要'));
  assert.ok(summary);
  assert.ok(!summary.properties.className?.includes('news-meta'));
  assert.equal(paragraphs.filter(p => p.properties.className?.includes('news-meta')).length, 2);
});
