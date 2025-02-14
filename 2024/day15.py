import os
import re
from collections import defaultdict, Counter, deque, namedtuple
import sympy

moves = []

DIRS = { '<' : (0,-1 ), '^': (-1,0), '>': (0,1) , 'v': (1,0)}
Y=0
X=0

def switch ( matrix, y,x, cy, cx):
    c = matrix[cy][cx]
    matrix[cy][cx] = matrix[y][x]
    matrix[y][x] = c

def print_matrix (matrix) :
    for i in range(len(matrix)):
        for c in matrix[i] :
            print (c, end='')
        print()

def main():
    matrix = []
    with open( "data/day15.txt") as file:
        lines = file.readlines()
    y=0
    for line in lines:

        if line.startswith("#"):
            matrix.append (list( line.strip()) )
            if line.find('@')> 0:
                Y=y
                X=line.find('@')
        elif len(line.strip()) >1 :
            for c in line.strip():
                moves.append (c)
        y +=1

    print ( matrix )
    print ( moves )
    y=Y
    x=X
    for m in moves:
        ym,xm = DIRS[ m]
        shifts =0
        while True:
            if matrix [ y+ym*(shifts+1) ][x+xm*(shifts+1) ] == '#':
                shifts=0
                break
            elif matrix[y + ym*(shifts+1)][x + xm*(shifts+1)] == '.':
                shifts += 1
                break
            else:
                shifts += 1
        while shifts>0:
            switch(matrix, y+ym*shifts ,x+xm*shifts,y+ym*(shifts-1),x+xm*(shifts-1) )
            shifts -=1
            if  shifts ==0:
                y = y + ym
                x = x + xm
        #print_matrix(matrix)

    p1 = 0
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if ( matrix[i][e] == 'O'):
                p1 += (i*100+e)
    print(p1)

    matrix = []
    with open( "data/day15.txt") as file:
        lines = file.readlines()
    y=0
    for line in lines:
        newline = []
        if line.startswith("#"):
            for c in line.strip():
                if c == '#':
                    newline.append ('#')
                    newline.append ('#')
                elif c =='O':
                    newline.append ('[')
                    newline.append (']')
                elif c == '@':
                    newline.append ('@')
                    newline.append ('.')
                    Y = y
                    X = line.find('@')*2
                else:
                    newline.append ('.')
                    newline.append ('.')
            matrix.append(newline)
        y +=1

    print ( len(matrix), Y,X, matrix )
    print ( moves )
    print_matrix(matrix)
    y=Y
    x=X

    for m in moves:
        print ( m ,y,x)
        ym, xm = DIRS[m]
        blocked = False
        test_queue = deque([(y, x)])
        shift_queue = deque([(y,x, '.')])
        shifted_queue = set()
        while test_queue:
            qy, qx = test_queue.popleft()
            if matrix[qy + ym ][qx + xm ] == '#':
                blocked = True
                break
            elif matrix[qy + ym ][qx + xm ] == '.':
                shift_queue.append ((qy+ym,qx+xm, matrix[qy][qx]))
                shifted_queue.add ((qy,qx))
                continue
            else:
                shifted_queue.add((qy, qx))
                shift_queue.append ((qy+ym,qx+xm, matrix[qy][qx]))
                test_queue.append((qy + ym, qx + xm ))
                if ym != 0 and matrix[qy + ym ][qx + xm ] == '[':
                    test_queue.append((qy+ym, qx+xm+1))
                if ym != 0 and matrix[qy+ym ][qx+xm ] == ']':
                    test_queue.append((qy+ym, qx+xm-1))
        if blocked == False:
            y += ym
            x += xm
            while shift_queue:
                qy, qx ,c = shift_queue.popleft()
                matrix[qy ][qx ] = c
                if (qy,qx) in shifted_queue:
                    shifted_queue.remove((qy,qx) )

            while shifted_queue:
                qy, qx  = shifted_queue.pop()
                matrix[qy ][qx ] = '.'

        #print_matrix(matrix)

    p2 = 0
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            if (matrix[i][e] == '['):
                p2 += (i * 100 + e)
    print(p2)

if __name__ == "__main__":
    main()