const puppeteer = require("puppeteer");

const launchOptions = {
  args: ["--no-sandbox"],
  headless: true,
};

const env = {
  FLAG: process.env.FLAG,
};

async function visit(url) {
  const browser = await puppeteer.launch(launchOptions);
  const page = await browser.newPage();

  console.log(`[visiter.visit] Visiting '${url}'`);

  const { host } = new URL(url);

  await page.setCookie({
    name: "FLAG",
    value: env.FLAG,
    httpOnly: false,
    domain: host,
    sameSite: "Strict",
  });

  await page.goto(url, { waitUntil: "load", timeout: 10000 });

  await new Promise((resolve) => setTimeout(resolve, 5000));

  console.log(`[visiter.visit] Done visiting`);

  await page.close();
  await browser.close();
}

module.exports = { visit };
