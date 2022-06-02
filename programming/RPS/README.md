# RPS

**`Author:`** [yh_0x7](https://github.com/yh-0x7)

## Description

- Alice and Bob were playing rock paper scissors.
- They forget to calculate the score at each round.
- Can you help them you determine the winner at the end of each game.
- The rules are simple:
- In each round if a player wins, he gets 3 points.
- If he wins in the next round he gets the double of the point he got in the last round.
- the output format will be the first letter of the player's name (A or B) followed
- by the score he got example : 'A:1337' Alice won and got 1337 points.
- in case of a drawn game just print 'D'


## Solution

```py
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
        if compare(p1,p2)==2:
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

```
