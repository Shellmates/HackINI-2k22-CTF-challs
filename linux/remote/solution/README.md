# remote

## Write-up

We notice that right after accessing the system using SSH, the shell prints `GOODBYE` message and gets closed.
We can read on the ssh manual page that we can specify a command to ssh to be executed instead of the default behaviour which starts an interactive login shell. When a login interactive shell is started, it executes the content of some startup files like ~/.bashrc, ~/.profile. A hypothesis that we can make is that one of the startup files prints the `GOODBYE` message and closes the shell right after it starts.
We can try to specify a command instead of leaving it blank, the command is going to be executed in a login **non** interactive shell, this will skip the execution of some startup files and maybe can skip the file that closes the shell, let's try it.
By executing : 
```bash
ssh ctf@remote -o ProxyCommand="openssl s_client -quiet -connect remote.challs.shellmates.club:443 -servername remote.challs.shellmates.club" ls
```
we get the listing of files and directories, so the command was executed succefully.

## Final payload
```bash
ssh ctf@remote -o ProxyCommand="openssl s_client -quiet -connect remote.challs.shellmates.club:443 -servername remote.challs.shellmates.club" cat flag.txt
```

## Flag

`shellmates{HOW_DID_U_M4d3_i7_HERE!}`

