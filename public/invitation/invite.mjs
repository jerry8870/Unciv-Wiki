const invitationPage = 'https://jerry8870.github.io/Unciv-Wiki/invite.html';

export function parseInvitation(search) {
  if (/%(?![0-9a-f]{2})/i.test(search)) throw new Error('Invalid encoding');
  const fields = search.replace(/^\?/, '').split('&');
  if (fields.length !== 2 || fields.some((field) => !field.includes('='))) throw new Error('Invalid parameters');
  const params = new URLSearchParams(search);
  if ([...params].length !== 2 || !params.has('gameId') || !params.has('server')) throw new Error('Invalid parameters');
  const gameId = params.get('gameId');
  if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(gameId)) throw new Error('Invalid game ID');
  const server = params.get('server');
  const url = new URL(server);
  const host = url.hostname.toLowerCase().replace(/\.$/, '');
  if (!/^https:\/\//i.test(server) || /[\s\\]/.test(server) || url.username || url.password || server.includes('?') || server.includes('#')
    || url.port === '0' || host.includes(':') || host.startsWith('[') || host === 'localhost'
    || /\.(localhost|local|lan|home\.arpa)$/.test(host) || host === 'home.arpa'
    || host.split('.').every((part) => /^(\d+|0x[0-9a-f]+)$/i.test(part))) throw new Error('Invalid server');
  const normalizedServer = server.replace(/\/+$/, '');
  const link = new URL(invitationPage);
  link.search = new URLSearchParams({ gameId, server: normalizedServer }).toString();
  return { gameId, server: normalizedServer, link: link.href };
}

const copy = {
  en: {
    title: 'Game invitation', intro: 'Open this invitation on your iPhone or iPad to view the multiplayer game.',
    gameLabel: 'Game ID', serverLabel: 'Server', copy: 'Copy invitation link', install: 'Install Unciv4iOS',
    manual: 'In the game, go to Multiplayer → Add game by Game ID, then paste this link.',
    browser: 'If WeChat keeps this page open, use its menu to open in your browser, or copy the link into the game. You can also long-press the link in Notes and choose to open it in Unciv4iOS, if available.',
    invalid: 'This invitation is invalid. Ask the creator to share a new link.',
    copied: 'Link copied. Open Unciv4iOS and paste it in Multiplayer.',
    select: 'Automatic copying is unavailable. Long-press the link below to copy it.',
  },
  zh: {
    title: '多人游戏邀请', intro: '在 iPhone 或 iPad 上打开邀请，查看这场多人游戏。',
    gameLabel: 'Game ID', serverLabel: '游戏服务器', copy: '复制邀请链接', install: '安装 Unciv4iOS',
    manual: '打开游戏 → 多人游戏 → 通过 Game ID 添加，再粘贴邀请链接。',
    browser: '如果微信停留在此页面，可通过右上角菜单用浏览器打开，或复制链接到游戏中粘贴。也可以把链接放入备忘录，长按后选择用 Unciv4iOS 打开（若有该选项）。',
    invalid: '邀请链接无效，请让创建者重新分享。',
    copied: '邀请链接已复制，请打开 Unciv4iOS，在多人游戏中粘贴。',
    select: '无法自动复制，请长按下方链接手动复制。',
  },
};

if (typeof document !== 'undefined') {
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  const text = copy[lang];
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
  document.title = `${text.title} · Unciv4iOS`;
  for (const [id, key] of Object.entries({ title: 'title', intro: 'intro', 'game-label': 'gameLabel', 'server-label': 'serverLabel', copy: 'copy', install: 'install', manual: 'manual', browser: 'browser', invalid: 'invalid' })) {
    document.getElementById(id).textContent = text[key];
  }
  try {
    if (location.hash) throw new Error('Invalid fragment');
    const invite = parseInvitation(location.search);
    document.getElementById('game-id').textContent = invite.gameId;
    document.getElementById('server').textContent = invite.server;
    document.getElementById('invitation').hidden = false;
    const fallback = document.getElementById('copy-fallback');
    fallback.setAttribute('aria-label', text.copy);
    fallback.value = invite.link;
    document.getElementById('copy').addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(invite.link);
        document.getElementById('status').textContent = text.copied;
        fallback.hidden = true;
      } catch {
        fallback.hidden = false;
        fallback.focus();
        fallback.select();
        document.getElementById('status').textContent = text.select;
      }
    });
  } catch {
    document.getElementById('intro').hidden = true;
    document.getElementById('invalid').hidden = false;
  }
}
