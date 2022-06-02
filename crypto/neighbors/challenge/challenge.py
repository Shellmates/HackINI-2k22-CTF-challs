#!/usr/bin/env python3

from gmpy2 import next_prime
from Crypto.Util import number

p = number.getPrime(2048)
q = next_prime(p)

e = 0x10001
N = p * q

with open("flag", "rb") as f:
    flag = number.bytes_to_long(f.read())

C = pow(flag, e, N)

with open("chall", "w") as f:
    f.write("\n".join([f"N : {N}", f"e : {e}", f"C : {C}"]))
