FROM buildkite/puppeteer

COPY app /app

WORKDIR /app

RUN npm install

RUN useradd ctf

USER ctf

ENTRYPOINT ["npm", "start"]
