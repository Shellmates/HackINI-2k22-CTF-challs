FLAG="ELF_m4G!c_ByTes_:D"
print(len(FLAG))
KEY="\x7f\x45\x4c\x46"
for i in range(len(FLAG)):
	print(f'\\x{hex(ord(FLAG[i])^ord(KEY[i%len(KEY)])).lstrip("0x")}',end="")