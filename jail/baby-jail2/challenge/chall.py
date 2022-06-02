#!/usr/bin/env python3


WELCOME = "I made my calculator app using Python. It's so dope. Try it out."
BLACKLIST = ["open", "input", "eval", "exec", "import", "getattr", "sh"]
def calc(op):
	try : 	
		res = eval(op)
	except :
		return print("Wrong operation")
	return print(f"{op} --> {res}")

def main():
	while True :
		inp = input(">> ")
		if any(bad in inp for bad in BLACKLIST) :
			print("Are you tying to hack me !!")
		else : 
			calc(inp)

if __name__ == '__main__':
	main()