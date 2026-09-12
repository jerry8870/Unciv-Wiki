import config from '../site.config.json' with { type: 'json' };
export default function remarkBase() {
  return (tree) => {
    function visit(node) {
      if (['link', 'image', 'definition'].includes(node.type) && node.url?.startsWith('/') && !node.url.startsWith('//') && !node.url.startsWith(config.base)) node.url = config.base + node.url.slice(1);
      // Authored figures use HTML for image dimensions and captions.
      if (node.type === 'html') node.value = node.value.replace(
        /\b(src|href)=(['"])(\/[^'"\s]*)\2/g,
        (match, attr, quote, url) => url.startsWith('//') || url.startsWith(config.base)
          ? match : `${attr}=${quote}${config.base}${url.slice(1)}${quote}`
      );
      node.children?.forEach(visit);
    }
    visit(tree);
  };
}
