#!/usr/bin/python3

from pwn import logging, remote
from binascii import hexlify, unhexlify
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad

host = "localhost"
port = 1337

logging.disable(logging.INFO)


def start():
    global r, flag_enc
    r = remote(host, port)
    flag_enc = (
        r.recvuntil(b"plaintext: ").decode().strip().split("\n")[-5].split("= ")[1]
    )
    #print(flag_enc);input()


def CBC_encrypt(inp):
    to_send = hexlify(inp)
    r.sendline(to_send)
    cbc_ct = r.recvuntil(b"Enter your ciphertext: ").decode().strip().split("\n")[0].split(": ")[1]
    return cbc_ct


def CBC_decrypt(inp):
    r.sendline(inp)
    cbc_pt = (
        r.recvuntil(b"Enter your plaintext: ")
        .decode()
        .strip()
        .split("\n")[0]
        .split(": ")[1]
    )
    return cbc_pt


def ECB_encrypt(inp):
    r.sendline(inp)
    cbc_ct = r.recvuntil(b"Bye").decode().strip().split("\n")[0].split(": ")[1]
    return cbc_ct


def stop():
    r.close()


if __name__ == "__main__":
    start()

    cbc_ct = CBC_encrypt(b"A" * 32)

    cbc_ct_blocks = [cbc_ct[i : i + 32].encode() for i in range(0, len(cbc_ct), 32)]

    cbc_pt = unhexlify(CBC_decrypt(cbc_ct_blocks[1]))
    #print(cbc_pt)
    IV = strxor(strxor(cbc_pt, b"A" * 16), unhexlify(cbc_ct_blocks[0]))
    #print(IV)
    ecb_payload = b""
    possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"
    assert len(possible_chars) == 65
    for char in possible_chars:
        ecb_payload += hexlify(strxor(IV, pad(char.encode(), 16)))
    #print(ecb_payload)
    ecb_ct = ECB_encrypt(ecb_payload)
    ecb_ct_blocks = [unhexlify(ecb_ct[i : i + 32]) for i in range(0, len(ecb_ct), 32)]

    d = {}
    for enc, char in zip(ecb_ct_blocks, possible_chars):
        d[enc] = char

    flag_enc_blocks = [
        unhexlify(flag_enc[i : i + 32]) for i in range(0, len(flag_enc), 32)
    ]
    #print(flag_enc_blocks)
    flag = ""
    for block in flag_enc_blocks:
        if d.get(block):
            flag += d[block]

    print(flag)

    stop()
