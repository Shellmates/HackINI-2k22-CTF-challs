const dotenv = require("dotenv");
dotenv.config({
  path: process.env.ENV_FILE ? process.env.ENV_FILE : ".env",
});

const env = {
  NODE_ENV: process.env.NODE_ENV || "development",
  NODE_PORT: process.env.NODE_PORT || 5000,
  APP_URL: process.env.APP_URL,
  HCAPTCHA_SECRET_KEY:
    process.env.HCAPTCHA_SECRET_KEY ||
    "0x0000000000000000000000000000000000000000",
  RECAPTCHA_SITE_KEY: process.env.RECAPTCHA_SITE_KEY,
  RECAPTCHA_SECRET_KEY: process.env.RECAPTCHA_SECRET_KEY,
  HCAPTCHA_VERIFY_URL: "https://hcaptcha.com/siteverify",
  RECAPTCHA_VERIFY_URL: "https://www.google.com/recaptcha/api/siteverify",
  WAF_BLACKLIST: "\t\n\x0b\x0c\r!#$%&(),.:;?@[\\]^_`{|}~",
  WAF_WHITELIST:
    " \"'*+-/0123456789<=>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
};

const visiter = require("./visiter");

const express = require("express");
const morgan = require("morgan");
const {
  expressCspHeader,
  SELF,
  STRICT_DYNAMIC,
  NONCE,
  NONE,
  UNSAFE_EVAL,
  DATA,
} = require("express-csp-header");
const Recaptcha = require("express-recaptcha").RecaptchaV2;
const recaptcha = new Recaptcha(
  env.RECAPTCHA_SITE_KEY,
  env.RECAPTCHA_SECRET_KEY
);

const app = express();

app.use(
  express.urlencoded({
    extended: false,
  })
);
app.use(morgan("combined"));
app.use(
  expressCspHeader({
    directives: {
      "base-uri": [SELF],
      "default-src": [SELF],
      "img-src": [SELF, DATA, "image/svg+xml"],
      "script-src": [UNSAFE_EVAL, NONCE, STRICT_DYNAMIC],
      "object-src": [NONE],
      "style-src": [NONCE, "unpkg.com", "cdn.jsdelivr.net", "cdn.jsdelivr.com"],
      "frame-src": [
        "https://www.google.com/recaptcha/",
        "https://recaptcha.google.com/recaptcha/",
      ],
    },
  })
);

let waf = (s) =>
  [...s]
    .map((c) => (env.WAF_WHITELIST.includes(c) ? c : "🐶"))
    .join("")
    .replace(/nonce/gi, "🐶🐶🐶🐶🐶");

app.set("view engine", "ejs");

app.get("/", (req, res) => {
  const { challenge } = req.query;
  let name;

  try {
    name = waf(JSON.parse(challenge).name);
  } catch (err) {
    name = undefined;
  }

  return res.render("pages/index", {
    nonce: req.nonce,
    title: name,
  });
});

app.post("/share", recaptcha.middleware.verify, async (req, res) => {
  if (req.recaptcha.error) {
    return res.status(400).send("Failed reCAPTCHA");
  }

  try {
    let { challenge } = req.body;

    if (typeof challenge === "string") {
      visiter
        .visit(`${env.APP_URL}/?challenge=${encodeURIComponent(challenge)}`)
        .catch((err) => {
          console.error(err);
        });
      return res.status(200).send("Challenge shared with admin");
    } else {
      return res.status(400).send("No challenge specified");
    }
  } catch (err) {
    console.error(err);
    return res.status(500).send("Internal server error");
  }
});

app.listen(env.NODE_PORT, () => {
  console.log(`App listening on ${env.APP_URL}`);
});
