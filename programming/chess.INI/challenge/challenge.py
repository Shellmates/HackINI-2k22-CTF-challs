#!/usr/bin/env python3
import random
FLAG = open('.passwd').read()
files = 'ABCDEFGH'
def place_rook(board,cli_board):
    x= random.randint(1,8)
    y= random.randint(1,8)
    cli_board[x-1][y-1]='K'
    return x,y

def place_target(board,cli_board,queen_position):
    x= random.randint(1,8)
    y= random.randint(1,8)
    while x == queen_position[0]  and y == queen_position[1]:
        x= random.randint(1,8)
        y= random.randint(1,8)
    cli_board[x-1][y-1]='T'
    return x,y

def place_pawns(board,cli_board,pawns_number,queen_position,target_position):
    pawns=[]
    while pawns_number:
        x= random.randint(1,8)
        y= random.randint(1,8)
        if (queen_position[0] == x and queen_position[1] == y) or (target_position[0]==x and target_position[1]==y):
            continue
        board[x][y]=1
        cli_board[x-1][y-1]='p'
        pawns.append((x,y))
        pawns_number-=1
    return pawns
def print_board(board):
    print(21*'_')
    for index,line in enumerate(board):
        print('|',str(8-index)+'|',' '.join(line),'|')
    print('| *|' ,' '.join(files[i] for i in range(8))+' |')
    print((21*'_')+'|')


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

def game():
    print('Welcome to chess.INI')
    for level in range(20):
        board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],]
        cli_board = [['.' for x in range(8)] for y in range(8)]
        end= rx,ry = place_rook(board,cli_board)
        start = tx,ty = place_target(board,cli_board,(rx,ry))
        pawns = place_pawns(board,cli_board,random.randint(0,5),(rx,ry),(tx,ty))
        print_board(cli_board)
        _input = int(input())
        _output = len(solver(board,start,end))
        if _input != _output:
            print('wrong path try again')
            exit(0)
    print(f'Gg mate here is your flag:{FLAG}')
game()
