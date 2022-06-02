#!/usr/bin/env python3

WHITELIST = 'abcdefghijklmnopqrstuvwxyz()'
NOT_ALLOWED_FUNCTIONS = ['input', 'exec', 'eval', 'breakpoint', 'help']

while True:
    expr = input("[ EVAL THIS FOR ME ] --> ")
    if any(char not in WHITELIST for char in expr ) or any(forbid in expr for forbid in NOT_ALLOWED_FUNCTIONS):
        print("NOPE!")
    else :
        if expr == "exit()" : exit()
        try : 
            eval(expr)
        except :
            print("Don't break it please.")


