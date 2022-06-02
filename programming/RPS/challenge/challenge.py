#!/usr/bin/env python3
import random
hand = ['R','P','S']
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

def game():
    for i in range(5,100):
        alice_hand = ''
        bob_hand = ''
        for j in range(i):
            alice_hand += random.choice(hand)
            bob_hand += random.choice(hand)
        print('Alice:',alice_hand)
        print('Bob:',bob_hand)
        result = input()
        if result == solver(alice_hand,bob_hand):
                print('Nice job!!!')
        else:
                print('Oh no...can you try again!!!' )
                exit(0)
    print('You nailed it here is your flag: shellmates{17\'5_J57_r0cK_P4P3r_5c1550R5}')

if __name__ == '__main__':
    game()
