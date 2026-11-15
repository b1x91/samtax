const fs = require('fs');
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');

const DIR = __dirname;
const OUT = path.join(DIR, 'shots');
const pages = process.argv.slice(2);

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',
    args: ['--no-sandbox'],
  });
  const ctx = await browser.newContext({
    viewport: { width: Number(process.env.W||1728), height: Number(process.env.H||746) },
    deviceScaleFactor: 2,
  });
  const page = await ctx.newPage();
  for (const p of pages) {
    await page.goto('file://' + path.join(DIR, p), { waitUntil: 'load' });
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(OUT, p.replace('.html', '.png')) });
    console.log('shot', p);
  }
  await browser.close();
})();
