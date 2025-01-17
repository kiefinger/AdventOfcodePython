import re
from itertools import product
from collections import defaultdict
dot = '.'
matrix = []
empty_list = []

def print_matrix():
    for l in matrix:
        print (''.join(l))

def main():
    fr = defaultdict(lambda: [])

    with open("data/day08.txt") as file:
        y=0
        for line in file.read().splitlines():
            l = list(line)
            matrix.append(  list(line) )
            x = 0
            for c in l:

                if ( c != dot and c !='#'):
                    fr[c].append( [y,x])
                x+=1
            y+=1

        print_matrix()

        print ( fr)
        for p in fr:
            possible = product(fr[p], repeat=2)
            for op in possible:
                if op[0] != op[1]:
                    disty = op[1][0] - op[0][0]
                    distx = op[1][1] - op[0][1]
                    low = [ op[0][0] - disty, op[0][1] - distx ]
                    high = [ op[1][0] + disty, op[1][1] + distx ]
                    if  low[0] >=0 and low[0] < len(matrix) and low[1] >=0 and low[1] < len(matrix[0]):
                        matrix[low[0]][low[1]] = '#'
                    if high[0] >=0 and high[0] < len(matrix) and high[1] >=0 and high[1] < len(matrix[0]):
                        matrix[high[0]][high[1]] = '#'

            print_matrix()

            total =0
            for i in range ( len(matrix)):
                for e in range ( len(matrix[0])):
                    if matrix[i][e]=='#':
                        total +=1

        print ( total )
        print ( "Part 2" )

        #part II
        for p in fr:
            print(p, fr[p])
            possible = product(fr[p], repeat=2)
            for op in possible:
                if op[0] != op[1]:
                    disty = op[1][0] - op[0][0]
                    distx = op[1][1] - op[0][1]

                    for n in range ( 1,max(len(matrix),len(matrix[0])),1):
                        low = [op[0][0] - disty*n, op[0][1] - distx*n]
                        high = [op[1][0] + disty*n, op[1][1] + distx*n]
                        if low[0] >= 0 and low[0] < len(matrix) and low[1] >= 0 and low[1] < len(matrix[0]):
                            matrix[low[0]][low[1]] = '#'
                        if high[0] >= 0 and high[0] < len(matrix) and high[1] >= 0 and high[1] < len(matrix[0]):
                            matrix[high[0]][high[1]] = '#'

        total = 0
        for i in range(len(matrix)):
            for e in range(len(matrix[0])):
                if matrix[i][e] != '.':
                    total += 1

        print(total)


if __name__ == "__main__":
    main()