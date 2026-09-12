import assert from 'node:assert/strict';
import { setupAnalytics } from '../src/analytics.js';
function fixture(id, initial, brokenStorage = false) {
  const nodes = Object.fromEntries(['status', 'accept', 'reject', 'revoke'].map((key) => [key, { hidden: false, textContent: '', addEventListener(name, callback) { this[name] = callback; } }]));
  const state = { choice: initial, scripts: [], reloads: 0, removed: false };
  const win = { location: { hostname: 'jerry8870.github.io', reload() { state.reloads++; } }, localStorage: { getItem() { if (brokenStorage) throw Error('blocked'); return state.choice; }, setItem(k, v) { if (brokenStorage) throw Error('blocked'); state.choice = v; } } };
  const doc = { cookie: '_ga=example', createElement() { return {}; }, head: { append(script) { state.scripts.push(script); } }, getElementById() { return { remove() { state.removed = true; } }; } };
  const panel = { dataset: { measurementId: id, locale: 'en', base: '/Unciv-Wiki/' }, querySelector(selector) { return nodes[selector.slice(6, -1)]; } };
  setupAnalytics(panel, win, doc);
  return { state, nodes, win, doc };
}
for (const id of ['', 'invalid']) {
  const f = fixture(id, 'granted');
  assert.equal(f.state.scripts.length, 0, 'No GA without valid configuration');
}
for (const choice of [null, 'denied']) {
  const f = fixture('G-LOCALTEST', choice);
  assert.equal(f.state.scripts.length, 0);
  f.nodes.reject.click();
  assert.equal(f.state.scripts.length, 0);
  assert.equal(f.state.choice, 'denied');
}
const f = fixture('G-LOCALTEST');
f.nodes.accept.click(); f.nodes.accept.click();
assert.equal(f.state.scripts.length, 1, 'Only one loader');
assert.equal(f.state.choice, 'granted');
assert.match(f.state.scripts[0].src, /^https:\/\/www.googletagmanager.com\/gtag\/js\?id=G-LOCALTEST$/);
assert.deepEqual(f.win.dataLayer.map((entry) => entry[0]), ['consent', 'js', 'config'], 'No duplicate custom click events');
f.nodes.revoke.click();
assert.equal(f.state.choice, 'denied');
assert.equal(f.win['ga-disable-G-LOCALTEST'], true);
assert.equal(f.state.removed, true);
assert.equal(f.state.reloads, 1);
assert.match(f.doc.cookie, /Max-Age=0/);
assert.equal(fixture('G-LOCALTEST', 'granted').state.scripts.length, 1, 'Remembered opt-in loads');
const blocked = fixture('G-LOCALTEST', null, true);
blocked.nodes.accept.click();
assert.equal(blocked.state.scripts.length, 1, 'Blocked storage does not break current-page consent');
console.log('Analytics gating: unconfigured, invalid ID, undecided, denied, accepted, revoke and blocked storage passed; no live requests sent.');
