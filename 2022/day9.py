import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

with open("data/day09-1.txt") as file:
    lines = file.readlines()
print (lines)

moves = []
for line in lines:
    line = line.rstrip()
    ove = line.split()
    moves.append([ove[0], int(ove[1 ] )])
print ( moves)

visited = {}
hx = 0
hy = 0
k = [ [hx,hy]  for i in range(10) ]

def mark (tx,ty):
    visited[ (tx,ty) ] = 1

def followto( hx, hy, i):

    if abs( hx - k[i][0]) > 1:
        if hx - k[i][0] >0:
            k[i][0] += 1
        if hx - k[i][0] <0:
            k[i][0] -= 1
        if abs( hy - k[i][1]) > 0:
            if hy - k[i][1] >0:
                k[i][1] += 1
            if hy - k[i][1] <0:
                k[i][1] -= 1

    if abs( hy - k[i][1]) > 1:
        if hy - k[i][1] >0:
            k[i][1] += 1
        if hy - k[i][1] <0:
            k[i][1] -= 1
        if abs( hx - k[i][0]) > 0:
            if hx - k[i][0] >0:
                k[i][0] += 1
            if hx - k[i][0] <0:
                k[i][0] -= 1

    if ( i==9):
        mark ( k[9][0], k[9][1])


for move in moves:
    print ( move[0], move[1])

    if (  move[0] =="R"):
        for i in range ( move[1]):
            k[0][0] +=1
            for e in range ( 10-1):
                followto (k[e][0], k[e][1] ,e+1)
    if (  move[0] =="L"):
        for i in range ( move[1]):
            k[0][0] -=1
            for e in range ( 10-1):
                followto (k[e][0], k[e][1] ,e+1)
    if (  move[0] =="U"):
        for i in range ( move[1]):
            k[0][1] -=1
            for e in range ( 10-1):
                followto (k[e][0], k[e][1] ,e+1)
    if (  move[0] =="D"):
        for i in range ( move[1]):
            k[0][1] +=1
            for e in range ( 10-1):
                followto (k[e][0], k[e][1] ,e+1)
    print ( k )
    print ( "H",  k[0][0], k[0][1] , "T", k[1][0], k[1][1] )


print ("Result 2: ", len(visited))
# Ergebnis 2: 2467