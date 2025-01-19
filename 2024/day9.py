import re
from itertools import product
from collections import defaultdict
dot = '.'
empty_list = []

def setup_matrix(line, matrix):
    index = 0
    matrix_index = 0
    for i in range(len(line)):
        # print ( "cahr", line[i])
        isFile = (i % 2 == 0)
        for e in range(int(line[i])):
            if isFile:
                # print("index", index)
                matrix[matrix_index] = index
            else:
                matrix[matrix_index] = -1
            matrix_index += 1
        if isFile:
            index += 1


def checksum(matrix ):
    total = 0
    for i in range(len(matrix) - 1):
        if matrix[i] != -1:
            # print ("add" , i*matrix[i])
            total += (i * matrix[i])
    return total

def main():

    with open("data/day09.txt") as file:
        line = file.read()
        print (len(line),line)

        matrix = {}
        setup_matrix(line, matrix)
        print ( matrix)

        e = len(matrix)-1
        i = 0
        while (i<e):
            while matrix[i]!= -1:
                i+=1
            while matrix[e]== -1:
                e-=1
            if  i<e:
                matrix[i] = matrix[e]
                matrix[e]=-1
            i+=1
            e-=1

        print ( checksum(matrix) )

        #part 2
        matrix = {}
        setup_matrix(line, matrix)
        print ( matrix)

        e = len(matrix)-1
        i = 0
        while (e>0):
            #print ( "E=",e)
            while matrix[e]== -1 :
                e-=1
            if e<=1:
                break
            e2=e
            while matrix[e-1] == matrix[e]:
                e-=1
            l = e2-e+1

            #search for free space

            i = 0;
            found = False
            empty = False
            while found == False and i< e:
                while matrix[i]!=-1:
                    i+=1
                b = 0
                while (i+b)< len(matrix) and matrix[i+b]==-1 :
                    b+=1

                if b>=l:
                    if e>i:
                        for s in range(l):
                            matrix[i+s] = matrix[e+s]
                            matrix[e+s] = -1
                            found = True
                            #print(matrix)
                else:
                    i+=1
            e-=1
        print(matrix)
        print(checksum(matrix))


if __name__ == "__main__":
    main()