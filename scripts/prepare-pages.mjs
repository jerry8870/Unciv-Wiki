import { cpSync, existsSync, readFileSync, rmSync } from 'node:fs';
import assert from 'node:assert/strict';

const config = JSON.parse(readFileSync(new URL('../site.config.json', import.meta.url), 'utf8'));
assert.equal(config.base, '/Unciv-Wiki/', 'Keep existing blog and invitation URLs');
const dist = new URL('../dist/', import.meta.url);
const output = new URL('../.pages-dist/', import.meta.url);
assert.ok(existsSync(new URL('index.html', dist)), 'Build the blog before packaging Pages');
rmSync(output, { recursive: true, force: true });
cpSync(new URL('../universal-links/root-site/', import.meta.url), output, { recursive: true });
cpSync(dist, new URL('Unciv-Wiki/', output), { recursive: true });

const association = JSON.parse(readFileSync(new URL('.well-known/apple-app-site-association', output), 'utf8'));
assert.deepEqual(association.applinks.details, [{
  appIDs: ['ZHMX53WRKQ.com.aishuati.unciv'],
  components: [{ '/': '/Unciv-Wiki/invite.html' }],
}]);
for (const file of ['index.html', 'invite.html', 'invitation/invite.mjs', 'sitemap-index.xml', 'sitemap-0.xml']) {
  assert.deepEqual(readFileSync(new URL('Unciv-Wiki/' + file, output)), readFileSync(new URL(file, dist)));
}
assert.ok(existsSync(new URL('.nojekyll', output)));
console.log('Pages package verified: domain-root association and unchanged /Unciv-Wiki/ URLs');
