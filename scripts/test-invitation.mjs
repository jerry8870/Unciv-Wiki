import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { parseInvitation } from '../public/invitation/invite.mjs';

const gameId = '4e2a8b72-3f04-4fa1-a7a9-81d6e3e0a092';
const params = (server = 'https://uncivserver.xyz') => new URLSearchParams({ gameId, server }).toString();

test('copied invitation retains its game and source server', () => {
  const invite = parseInvitation('?' + params('https://example.com:8443/multiplayer/'));
  assert.equal(invite.gameId, gameId);
  assert.equal(invite.server, 'https://example.com:8443/multiplayer');
  assert.equal(new URL(invite.link).pathname, '/Unciv-Wiki/invite.html');
  assert.equal(new URL(invite.link).hostname, 'jerry8870.github.io');
  assert.equal(new URL(invite.link).searchParams.get('server'), invite.server);
});

test('ambiguous or malformed invitation parameters are rejected', () => {
  for (const search of ['', '?gameId=bad&server=https%3A%2F%2Fexample.com',
    '?' + params() + '&gameId=' + gameId, '?' + params() + '&playerId=' + gameId,
    '?' + params() + '&', '?gameId=' + gameId + '&server=%ZZ',
    '?gameId=' + gameId + '&server=https%253A%252F%252Fexample.com']) {
    assert.throws(() => parseInvitation(search), undefined, search);
  }
});

test('server URLs never carry credentials or target local networks', () => {
  for (const server of ['http://example.com', 'https://localhost', 'https://127.0.0.1',
    'https://10.0.0.1', 'https://[::1]', 'https://2130706433', 'https://0x7f000001',
    'https://printer.local', 'https://home.arpa', 'https://a.home.arpa',
    'https://user:password@example.com', 'https://example.com?password=secret',
    'https://example.com#secret', 'https://example.com:0', 'https://example.com\n']) {
    assert.throws(() => parseInvitation('?' + params(server)), undefined, server);
  }
});

test('domain-root association is limited to the invitation page', () => {
  const file = new URL('../universal-links/root-site/.well-known/apple-app-site-association', import.meta.url);
  const association = JSON.parse(readFileSync(file, 'utf8'));
  assert.deepEqual(association.applinks.details, [{
    appIDs: ['ZHMX53WRKQ.com.aishuati.unciv'],
    components: [{ '/': '/Unciv-Wiki/invite.html' }],
  }]);
  const html = readFileSync(new URL('../public/invite.html', import.meta.url), 'utf8');
  assert.match(html, /name="referrer" content="no-referrer"/);
  assert.match(html, /name="robots" content="noindex, nofollow"/);
  assert.match(html, /id="copy-fallback"[^>]*readonly hidden/);
  assert.doesNotMatch(html, /unciv4ios:\/\//);
});
