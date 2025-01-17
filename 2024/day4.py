import re

matrix = []

dirs = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0, -1],

    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

pairs = [
    ['M', 'M', 'S', 'S'],
    ['M', 'S', 'M', 'S'],
    ['S', 'S', 'M', 'M'],
    ['S', 'M', 'S', 'M'],
]

def checkIndex ( y, x):
    if y >= 0 and y < len(matrix):
        if x >= 0 and x < len(matrix[0]):
            return True;
    return False

def checkChar ( y, x, char):
    if checkIndex(y,x) :
        if matrix[y] [x] == char:
            return True
    return False

def main():

    with open("data/day04.txt") as file:

        total_max = 0
        total = 0
        m = []

        for line in file.read().splitlines():
            linearray = [ *line ]
            matrix.append(linearray)

#        print("total: ", matrix,lenx,leny)

        for i in range (len(matrix)):
            for e in range (len(matrix[0])):
                if matrix [i][e] == "X":
                    for p in dirs:
                        if checkIndex(i + p[0],e + p[1]) and matrix[i + p[0]] [e + p[1]] == 'M':
                            if checkIndex(i + 2*p[0], e + 2*p[1]) and matrix[i + 2*p[0]] [e + 2*p[1]] == 'A':
                                if checkIndex(i + 3*p[0], e + 3*p[1]) and matrix[i + 3*p[0]] [e + 3*p[1]] == 'S':
                                    total +=1

        print(total) #2530
        total = 0

        for i in range (len(matrix)):
            for e in range (len(matrix[0])):
                if matrix [i][e] == "A":
                    for pair in pairs:
                        if checkChar(i -1, e -1, pair[0]):
                            if checkChar(i - 1, e + 1, pair[1]):
                                if checkChar(i +1, e -1, pair[2]):
                                    if checkChar(i + 1, e + 1, pair[3]):
                                        total +=1


        print(total) #2530


if __name__ == "__main__":
    main()