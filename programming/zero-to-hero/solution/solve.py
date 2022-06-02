#!/usr/bin/env python3


# 1 - Build graph skill --> (skills needed) 
# 2 - Direct application of topological sorting 

import graphlib
from pwn import *

begin, l = 9, 10
host, port = "zero-to-hero.challs.shellmates.club", 443

def make_graph(r):
    dpnds = {}
    for line in r : 
        skill, skills = line.split(":")
        skill = skill[begin:begin+l]
        skills = skills.strip()
        if skills :
            skills = skills.split("-")
        else :
            skills = []
        dpnds[skill] = skills
    return dpnds

def main():
    p = remote(host, port, ssl=True)
    p.recvuntil("randomly\n\n")
    for i in range(90):
        r = p.recvuntil('\nPath -> ',drop=True).decode().split("\n")
        g = make_graph(r)
        try : 
            result = "-".join(graphlib.TopologicalSorter(g).static_order())
        except graphlib.CycleError :
            result = "impossible"
        p.sendline(result)
    p.interactive()

if __name__ == '__main__':
    main()