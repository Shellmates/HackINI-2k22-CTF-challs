#!/usr/bin/python
from pwn import *
from gmpy2 import iroot
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
import math

s = remote('rsimple.challs.shellmates.club',443,ssl=True)

r = 17

n = [None]*r
c = [None]*r
t = [None]*r

for i in range(r):
    s.recvuntil(b'>> ') 
    s.sendline(b'3')
    s.recvline()
    p=s.recvline()
    n[i] = int(p.split(b' ')[6])
    p = s.recvline()
    c[i] = int(p.split(b' ')[4][:-1].decode())

for i in range(r):
    N = math.prod([n[j] for j in list(set(range(r))-{i})])
    t[i] = c[i]*N*inverse(N,n[i])

c = sum(t)%math.prod(n)

print(long_to_bytes(iroot(c,17)[0]))

s.close()




