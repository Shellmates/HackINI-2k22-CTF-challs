#!/usr/bin/env python3


def decode(char):
    n = ord(char)
    if n < 32:
        return chr(n + 32)
    elif n < 64:
        return chr(n + 64)
    elif n < 96:
        return chr(n - 64)
    else:
        return chr(n - 32)


with open("enc", "rb") as f:
    enc = f.read().decode().split("\n")[1]

flag = "".join(decode(char) for char in enc)
print(f"The flag : {flag}")
