# agentDNS

## Write-up

This is a basic DNS exfiltration attack, you will first need to read about it a little bit, or watch this simple [explanation](https://www.youtube.com/watch?v=fQ4Y8napHzw)
First we retreive all DNS qureies via tshark, then we take one line per two, cause one of them is the actual query and the second is just a response.

```bash
$ tshark -r capture.pcapng -T fields -e dns.qry.name > hex.txt
```
We retreive the hexdump with a simple python script!
```python
import binascii

lines=open("hex.txt","r").readlines()
byte=""
i=True
for l in lines:
	if(i):
		byte+=l.replace(".secret.base","").replace("\n","")
	i=not i

open("data","wb").write(binascii.unhexlify(byte))

```
We can see that data is a zip file, unzip it and read the flag!

```bash
$ file data
data: Zip archive data, at least v2.0 to extract
$ unzip data
$ cat data.txt
```



## Flag

`shellmates{DN$_exf1!tr4Too0oO0r}`