/** Normalize generated RSS Markdown at render time, including historical reports. */
export default function newsLayout() {
  return (tree) => {
    const content = (node) => node.value ?? (node.children ?? []).map(content).join('');
    const element = (tagName, children, className) => ({
      type: 'element', tagName, properties: className ? { className: [className] } : {}, children,
    });
    if (!tree.children.some(node => node.tagName === 'p' && /^来源[：:]/.test(content(node).trim()))) return;

    const headings = tree.children.filter(node => node.tagName === 'h3');
    const firstBlockquote = tree.children.find(node => node.type === 'element');
    const walk = (node, fn) => { fn(node); for (const child of node.children ?? []) walk(child, fn); };
    if (firstBlockquote?.tagName === 'blockquote') {
      firstBlockquote.properties ??= {};
      firstBlockquote.properties.className = ['news-digest'];
      walk(firstBlockquote, node => {
        if (node.tagName !== 'li') return;
        const heading = headings.find(h => content(h).trim() === content(node).trim());
        if (heading?.properties?.id && !node.children.some(child => child.tagName === 'a')) {
          node.children = [{ ...element('a', node.children), properties: { href: `#${heading.properties.id}` } }];
        }
      });
    }

    let entry;
    const output = [];
    for (const node of tree.children) {
      if (node.tagName === 'h2') entry = undefined;
      if (node.tagName === 'h3') {
        entry = element('section', [], 'news-entry');
        output.push(entry);
      }
      const target = entry ? entry.children : output;
      if (node.tagName === 'p' && /^(来源|发布时间)[：:]/.test(content(node).trim())) {
        const parts = [];
        let children = [];
        const flush = () => {
          if (children.some(child => child.type !== 'text' || child.value.trim())) {
            const isMeta = /^(来源|发布时间)[：:]/.test(children.map(content).join('').trim());
            parts.push(element('p', children, isMeta ? 'news-meta' : undefined));
          }
          children = [];
        };
        for (const child of node.children) {
          if (child.type === 'text' && children.length === 0) {
            const metadata = child.value.match(/^((?:来源|发布时间)[：:][^\n]*)(\n[\s\S]*)$/);
            if (metadata) {
              children.push({ ...child, value: metadata[1] });
              flush();
              children.push({ ...child, value: metadata[2] });
              continue;
            }
          }
          if (child.tagName === 'img') {
            flush();
            child.properties ??= {};
            child.properties.loading = 'lazy';
            child.properties.decoding = 'async';
            child.properties.alt ||= entry ? content(entry.children[0]) : '新闻配图';
            parts.push(element('p', [child], 'news-image'));
          } else {
            if (child.tagName === 'strong' && /^(来源|发布时间)[：:]/.test(children.map(content).join('').trim())) flush();
            children.push(child);
          }
        }
        flush();
        target.push(...parts);
      } else {
        target.push(node);
      }
    }
    tree.children = output;
  };
}
