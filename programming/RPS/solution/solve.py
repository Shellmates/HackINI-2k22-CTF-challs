from pwn import *
def solver(player1,player2):
    def compare(x,y):
        if x=='R' and y=='S':
            return 0
        elif x== 'P' and y=='R':
            return 0
        elif x== 'S' and y=='P':
            return 0
        if y=='R' and x=='S':
            return 1
        elif y== 'P' and x=='R':
            return 1
        elif y== 'S' and x=='P':
            return 1
        else:
            return -1
    score_player1 = 0
    score_player2 = 0
    combo1 = 1
    combo2 = 1
    for p1,p2 in zip(player1,player2):
        if compare(p1,p2)==0:
            score_player1+= 3*combo1
            combo1*=2
            combo2=1
        elif compare(p1,p2)==1:
            score_player2+= 3*combo2
            combo2*=2
            combo1=1
        else:
            score_player1+=1
            score_player2+=1
            combo1=1
            combo2=1
    return 'D' if score_player1==score_player2 else [f'A:{score_player1}',f'B:{score_player2}'][score_player1<score_player2]
p = remote('rps.challs.shellmates.club',443, ssl=True)
while True:
        try:
            a = p.recvline().decode()#.strip()[7:]        
            b = p.recvline().decode()#.strip()[5:]
            p.sendline(solver(a.strip()[7:],b.strip()[5:]))
            p.recvline()
        except:
            print(a)
            exit()