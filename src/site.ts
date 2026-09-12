import config from '../site.config.json';
export { config };
export const withBase = (path: string) => path.startsWith('/') && !path.startsWith('//') && !path.startsWith(config.base) ? config.base + path.slice(1) : path;
export const localUrl = (path: string, zh = false) => config.base + (zh ? 'zh/' : '') + path;
