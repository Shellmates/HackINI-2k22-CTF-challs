#!/usr/bin/env python3


BLACKLIST="!\"#$%&'*+,-./0123456789:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
while 1:
        exp=input('>>> ')
        check1 = all(ord(i)<127 for i in exp)
        check2 = all(i not in exp for i in BLACKLIST)
        check3 = exp.find('input')+exp.find('eval')+exp.find('exec')
        if check1 and check2 and check3==-3:
            try:
                eval(exp)
            except Exception as e:
                print(e)
        else:
            print('BAD!')
