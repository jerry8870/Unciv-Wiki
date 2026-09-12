/** Load GA only after opt-in. Outbound clicks are GA4 enhanced-measurement events. */
export function setupAnalytics(panel, win = window, doc = document) {
  const id = panel.dataset.measurementId || '';
  const configured = /^G-[A-Z0-9]+$/.test(id);
  const key = 'unciv-wiki-analytics';
  const zh = panel.dataset.locale === 'zh';
  let choice;
  try { choice = win.localStorage.getItem(key); } catch { /* Storage may be unavailable. */ }
  let loaded = false;
  function render() {
    panel.querySelector('[data-status]').textContent = !configured
      ? (zh ? '本站尚未配置分析统计，当前不加载 GA4。' : 'Analytics is not configured. GA4 is not loaded.')
      : choice === 'granted'
        ? (zh ? '你已同意分析统计，可随时撤回。' : 'You accepted analytics. You can withdraw at any time.')
        : (zh ? '分析统计未开启。仅在你同意后记录页面访问和外链点击。' : 'Analytics is off. Page views and outbound clicks are recorded only after you accept.');
    panel.querySelector('[data-accept]').hidden = !configured || choice === 'granted';
    panel.querySelector('[data-reject]').hidden = choice === 'granted';
    panel.querySelector('[data-revoke]').hidden = choice !== 'granted';
  }
  function load() {
    if (!configured || choice !== 'granted' || loaded) return;
    loaded = true;
    win['ga-disable-' + id] = false;
    win.dataLayer = win.dataLayer || [];
    win.gtag = function () { win.dataLayer.push(arguments); };
    win.gtag('consent', 'default', { analytics_storage: 'granted', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });
    win.gtag('js', new Date());
    win.gtag('config', id, { allow_google_signals: false, allow_ad_personalization_signals: false, cookie_path: panel.dataset.base });
    const script = doc.createElement('script');
    script.id = 'wiki-ga4';
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    doc.head.append(script);
  }
  function save(value) {
    choice = value;
    try { win.localStorage.setItem(key, value); } catch { /* Keep this page usable without storage. */ }
    render();
  }
  panel.querySelector('[data-accept]').addEventListener('click', () => { save('granted'); load(); });
  panel.querySelector('[data-reject]').addEventListener('click', () => save('denied'));
  panel.querySelector('[data-revoke]').addEventListener('click', () => {
    save('denied');
    win['ga-disable-' + id] = true;
    doc.getElementById('wiki-ga4')?.remove();
    for (const cookie of doc.cookie.split(';')) {
      const name = cookie.split('=')[0].trim();
      if (!name.startsWith('_ga')) continue;
      for (const path of ['/', panel.dataset.base]) {
        const expired = `${name}=; Max-Age=0; path=${path}; SameSite=Lax`;
        doc.cookie = expired;
        // GA's auto domain may use a parent domain.
        const parts = win.location.hostname.split('.');
        for (let i = 0; i < parts.length - 1; i++) doc.cookie = expired + '; domain=.' + parts.slice(i).join('.');
      }
    }
    // Unload GA's event listeners as well as its script element.
    win.location.reload();
  });
  render();
  load();
}
