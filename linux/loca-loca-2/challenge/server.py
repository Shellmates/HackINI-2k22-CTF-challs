#!/usr/bin/env python3

import asyncio
import websockets
import subprocess
import os
import tempfile
from werkzeug.utils import secure_filename
import jinja2

HOST, PORT = "0.0.0.0", 8765
DEFAULT_FILENAME = "file"
MAX_CONTENT_LENGTH = 5 * 2**10
DATE_CMD = "/bin/date"
TURNS = 10
PING_TIMEOUT = 2 * 60

BLACKLIST = {
    "SEC-WEBSOCKET-KEY-VERSION",
    "LD_AUDIT",
    "TMPDIR",
    "LD_DEBUG",
    "LD_AOUT_LIBRARY_PATH",
    "USER-AGENT",
    "HOST",
    "NLSPATH",
    "LD_PROFILE",
    "LD_AOUT_PRELOAD",
    "LD_DYNAMIC_WEAK",
    "GCONV_PATH",
    "UPGRADE",
    "RESOLV_HOST_CONF",
    "LD_PRELOAD",
    "TZDIR",
    "LOCALDOMAIN",
    "NIS_PATH",
    "LD_SHOW_AUXV",
    "CONNECTION",
    "SEC-WEBSOCKET-EXTENSIONS",
    "LD_DEBUG_OUTPUT",
    "LD_ORIGIN_PATH",
    "RES_OPTIONS",
    "MALLOC_TRACE",
    "HOSTALIASES",
    "SEC-WEBSOCKET-KEY",
    "LD_USE_LOAD_BIAS",
    "LD_LIBRARY_PATH",
    "GETCONF_DIR",
    "SEC-WEBSOCKET-VERSION",
}


def upload(filename, content):
    sf = secure_filename(filename)
    sf = sf if sf != "" else DEFAULT_FILENAME
    tmpdir = tempfile.mkdtemp()
    filepath = os.path.join(tmpdir, sf)
    os.chmod(tmpdir, 0o700)
    with open(filepath, "wb") as f:
        f.write(content[:MAX_CONTENT_LENGTH])
    os.chmod(filepath, 0o700)
    return tmpdir, filepath


def date(env):
    with subprocess.Popen(
        DATE_CMD,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=os.environ | env,
    ) as p:
        output, error = (x.strip().decode() for x in p.communicate())
    return output, error


async def handler(ws):
    done = False
    uploaded = False
    tmpdir = None
    filepath = None
    i = 0

    print(f"Connection received: {ws.id}")

    new_env = {}
    for header in ws.request_headers:
        if header.upper() not in BLACKLIST:
            new_env[header.upper()] = ws.request_headers[header]

    try:
        while not done and i < TURNS:
            action = await ws.recv()
            if action == "UPLOAD":
                if uploaded:
                    await ws.send("One upload per connection")
                else:
                    uploaded = True
                    filename = await ws.recv()
                    content = await ws.recv()
                    tmpdir, filepath = upload(filename, content)
                    await ws.send(f"Content uploaded to {filepath}")
            elif action == "DATE":
                output, _ = date(new_env)
                template = jinja2.Template(f"Date: {output}")
                await ws.send(template.render())
            elif action == "EXIT":
                done = True
            else:
                await ws.send(f"Unrecognized action: '{action}'")
            i += 1
    finally:
        if tmpdir != None:
            os.remove(filepath)
            os.rmdir(tmpdir)
        print(f"Connection closed {ws.id}")


async def main():
    async with websockets.serve(handler, HOST, PORT, ping_timeout=PING_TIMEOUT):
        await asyncio.Future()


asyncio.run(main())
