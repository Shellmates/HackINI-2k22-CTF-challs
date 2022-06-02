#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify
from Crypto.Util.strxor import strxor
import os
from time import sleep
BLOCK_SIZE = 16


key = os.urandom(BLOCK_SIZE)
iv = os.urandom(BLOCK_SIZE)

FLAG = "shellmates{1_h0p3_y0u_r3tr13v3d_th3_1V_4nd_3ncrypt3d_477_p0551b73_ch4r5}"

cbc = AES.new(key, AES.MODE_CBC, iv)


def flag_encrypt():
    pt_blocks = [pad(i.encode(), BLOCK_SIZE) for i in FLAG]

    ct_blocks = []
    for block in pt_blocks:
        cbc = AES.new(key, AES.MODE_CBC, iv)
        ct = cbc.encrypt(block)
        ct = hexlify(ct).decode()
        ct_blocks.append(ct)

    return ct_blocks


def cbc_encrypt(inp):
    inp = pad(unhexlify(inp), BLOCK_SIZE)
    cbc = AES.new(key, AES.MODE_CBC, iv)
    ct = cbc.encrypt(inp)
    return hexlify(ct)


def cbc_decrypt(inp):
    inp = unhexlify(inp)
    cbc = AES.new(key, AES.MODE_CBC, iv)
    pt = cbc.decrypt(inp)
    return hexlify(pt)


def ecb_encrypt(inp):
    inp = pad(unhexlify(inp), BLOCK_SIZE)
    cbc = AES.new(key, AES.MODE_ECB)
    ct = cbc.encrypt(inp)
    return hexlify(ct)


if __name__ == "__main__":
    sleep(2)
    flag_enc_blocks = flag_encrypt()
    flag_enc = "".join(flag_enc_blocks)
    print(
        f"magically encrypted flag = {flag_enc}\n\rCan you decrypt it with only these 3 specific steps ? (input should be in hex)"
    )

    print("1) CBC_encrypt:\n")

    cbc_pt = input("\rEnter your plaintext: ")
    try:
        cbc_ct = cbc_encrypt(cbc_pt).decode()
    except:
        print("You screwed up, Bye")
        exit()
    print(f"Here is your CBC ciphertext: {cbc_ct}")

    print("2) CBC_decrypt:\n")
    cbc_ct = input("\rEnter your ciphertext: ")
    try:
        cbc_ct_blocks = [cbc_ct[i : i + 32] for i in range(0, len(cbc_ct), 32)]
        if any(
            [
                bool(flag_enc_blocks[i] in cbc_ct_blocks)
                for i in range(len(flag_enc_blocks))
            ]
        ):
            print("Hack attempt flagged, bye!")
            exit()

        cbc_pt = cbc_decrypt(cbc_ct).decode()
    except:
        print("You screwed up, Bye")
        exit()
    print(f"Here is your CBC plaintext: {cbc_pt}")

    print("3) ECB_encrypt:\n")
    ecb_pt = input("\rEnter your plaintext: ")
    try:
        ecb_ct = ecb_encrypt(ecb_pt).decode()
    except:
        print("You screwed up, Bye")
        exit()

    print(f"Here is your ECB ciphertext: {ecb_ct}")

    print("I hope you got it, Bye")
