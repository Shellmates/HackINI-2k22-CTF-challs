#!/usr/bin/env python3

import asyncio
import websockets
import sys

TURNS = 10
HEADERS = {"LC_TIME": "en_US"}
MAX_CONTENT_LENGTH = 5 * 2**10


async def upload_action(ws, filename, content):
    await ws.send("UPLOAD")
    await ws.send(filename)
    await ws.send(content)
    buf = await ws.recv()
    filepath = buf.split("Content uploaded to ", 1)[-1]
    return filepath


async def date_action(ws):
    await ws.send("DATE")
    buf = await ws.recv()
    date = buf.split("Date: ", 1)[-1]
    return date


async def exit_action(ws):
    await ws.send("EXIT")


ACTIONS = [
    "UPLOAD",
    "DATE",
    "EXIT",
]

UPLOADED = False


def menu():
    global UPLOADED

    option = -1
    print("1. Upload")
    print("2. Date")
    print("3. Exit\n")
    while not (1 <= option <= 3) or (option == 1 and UPLOADED):
        try:
            option = int(input("Option: "))
        except ValueError:
            pass
    UPLOADED = option == 1
    return ACTIONS[option - 1]


async def client():
    async with websockets.connect(f"ws://{HOST}:{PORT}", extra_headers=HEADERS) as ws:
        i = 0
        done = False

        while not done and i < TURNS:
            action = menu()
            if action == "UPLOAD":
                while True:
                    filename = input("Filename: ")
                    try:
                        with open(filename, "rb") as f:
                            content = f.read()
                        break
                    except Exception as e:
                        print(e, file=sys.stderr)
                assert len(content) <= MAX_CONTENT_LENGTH
                filepath = await upload_action(ws, filename, content)
                print(f"File path: {filepath}")
            elif action == "DATE":
                date = await date_action(ws)
                print(f"Date: {date}")
            elif action == "EXIT":
                done = True
                await exit_action(ws)
            i += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            f"Usage: {sys.argv[0]} HOST PORT [HEADERS...]\nExample usage: {sys.argv[0]} docker.shellmates.club 31337 LC_TIME=fr_FR",
            file=sys.stderr,
        )
        sys.exit(1)

    HOST, PORT = sys.argv[1], sys.argv[2]

    for arg in sys.argv[3:]:
        header, value = arg.split("=", 1)
        HEADERS[header] = value

    asyncio.run(client())
