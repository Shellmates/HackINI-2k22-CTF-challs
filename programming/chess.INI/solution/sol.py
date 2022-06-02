from concurrent.futures import process
from os import sendfile
from pwn import *



#conn = remote('chess-ini.challs.shellmates.club',443,ssl = True)
conn = process('../challenge/challenge.py')
def solver(a,start,end):
    m=[]
    def make_step(k):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:
                        m[i-1][j] = k + 1
                    if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:
                        m[i][j-1] = k + 1
                    if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:
                        m[i+1][j] = k + 1
                    if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:
                        m[i][j+1] = k + 1

                    if i>0 and j>0 and m[i-1][j-1] == 0 and a[i-1][j-1] == 0:
                        m[i-1][j-1] = k + 1
                    if i<len(m)-1 and j<len(m[i])-1 and m[i+1][j+1] == 0 and a[i+1][j+1] == 0:
                        m[i+1][j+1] = k + 1
                    if i<len(m)-1 and j>0 and m[i+1][j-1] == 0 and a[i+1][j-1] == 0:
                        m[i+1][j-1] = k + 1
                    if j<len(m[i])-1 and i>0 and m[i-1][j+1] == 0 and a[i-1][j+1] == 0:
                        m[i-1][j+1] = k + 1


    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1

    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)

    i, j = end
    k = m[i][j]
    the_path = [(i,j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k-1:
            i, j = i-1, j
            the_path.append((i, j))
            k-=1
        elif j > 0 and m[i][j - 1] == k-1:
            i, j = i, j-1
            the_path.append((i, j))
            k-=1
        elif i < len(m) - 1 and m[i + 1][j] == k-1:
            i, j = i+1, j
            the_path.append((i, j))
            k-=1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
            i, j = i, j+1
            the_path.append((i, j))
            k -= 1


        elif i>0 and j>0 and m[i - 1][j-1] == k-1:
            i, j = i-1, j-1
            the_path.append((i, j))
            k-=1

        elif i<len(m)-1 and j<len(m[i])-1 and m[i+1][j+1] == k-1:
            i, j = i+1, j+1
            the_path.append((i, j))
            k-=1

        elif  i<len(m)-1 and j>0 and m[i+1][j-1] == 0 and  m[i + 1][j] == k-1:
            i, j = i+1, j-1
            the_path.append((i, j))
            k-=1
        elif j<len(m[i])-1 and i>0 and m[i-1][j + 1] == k-1:
            i, j = i-1, j+1
            the_path.append((i, j))
            k -= 1
    return the_path
print(conn.recvuntil('INI\n'))
while True:
    L = [i[5:-2].decode().split() for i in conn.recv().replace(b'.',b'0').replace(b'p',b'1').split(b'\n')[1:-3]]
    for i in range(8):
        for j in range(8):
            if L[i][j] == 'K':
                xk,yk = i,j
            elif L[i][j] == 'T':
                xt,yt = i,j

    for i in range(8):
        for j in range(8):
            if L[i][j] == 'K':
                L[i][j]='0'
            elif L[i][j] == 'T':
                L[i][j]='0'
    L = (list([list(map(int,i)) for i in  L]))
    print(L)
    conn.sendline(str(len(solver(L,(xk,yk),(xt,yt)))).encode())
conn.close()