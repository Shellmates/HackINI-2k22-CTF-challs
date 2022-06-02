#!/usr/bin/env python
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse, getPrime
from gmpy2 import iroot
from flag import FLAG

# FLAG = bytes_to_long(b'shellmates{this the test flag}')

def decrypt():
    return "This feature is under maintainance"

def encrypt( pt:bytes ):
    m = bytes_to_long(pt)
    n = getPrime(256) * getPrime(256)
    e = 17
    c = pow(m,e,n)
    print(f"Btw here is your public key: {n}")
    return c

def main():
    print('Welcom blah blah blah blah')
    while True:
        print('now choose your side:\n\t1) encrypt data\n\t2) decrypt data\n\t3) get the flag\n\t4) exit')
        choice = int(input('>> '))
        if choice == 1: 
            print('What do you want to encrypt?')
            pt = input('> ').encode()
            print(encrypt(pt))
            
        elif choice == 2:

            print(decrypt())
            
        elif choice == 3:
            print(f"Did you really tought I would easily give you the flag, but since you asked for it here is the encrypted flag: ")
            print(f'The encrypted flag is: {encrypt(FLAG)}')
            
        else:
            break 
        
if __name__ == "__main__":
        main()