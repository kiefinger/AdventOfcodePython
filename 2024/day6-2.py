from collections import defaultdict
import copy

matrix = []

moves = [
    [ -1 ,0 ],
    [ 0, 1 ],
    [ 1, 0],
    [0, -1]
]

move_index = 0

def print_matrix():
    for a in range(len(matrix)):
        print (''.join( matrix[a]))


def main():
    with open("data/day06.txt") as file:
        rulesComming = True

        countx = 0
        i =0
        for line in file.read().splitlines():
            countx += line.count('#')
            matrix.append ( list ( line))
            if  line.find('^') > 0:
                starty = i
                startx = line.find('^')

            i+=1
        print (countx)
        print ( starty,startx, len(matrix), len(matrix[0]), matrix )
        matrix[starty][startx] = '.'
        obstructions = 0
        non_obstructions = 0;
        tests = 0
        not_to_be_testes = 0
        for oiy in range ( len(matrix)):
            for oix in range ( len(matrix[0])):
                if (oiy == starty and oix == startx) or matrix[oiy][oix] == '#':
                    #print ( "not to be testeed", oiy, oix)
                    not_to_be_testes +=1
                else:
                    #print("check point", oiy, oix)

                    #set extra block and check the matrix
                    matrix[oiy][oix] ='#'
                    y=starty
                    x=startx
                    move_index = 0
                    visits = 0
                    count_moves = 0

                    while count_moves < 30000:
                        #print ( "check" ,y,x )
                        nexty = y + moves[move_index][0]
                        nextx = x + moves[move_index][1]

                        if nexty < 0 or nexty > len(matrix)-1:
                            #print ( "nexty", nexty)
                            #print_matrix()
                            break
                        if nextx < 0 or nextx > len(matrix[0])-1:
                            #print ("nextx", nextx)
                            #print_matrix()
                            break
                        #print("check", y, x, nexty, nextx)
                        if matrix[ nexty] [nextx] == '#' :
                            move_index = (move_index +1) % 4
                            nexty = y + moves[move_index][0]
                            nextx = x + moves[move_index][1]
                        y = nexty
                        x = nextx
                        count_moves+=1
                        #print (y,x)
                    if ( count_moves < 30000):
                        non_obstructions+=1
                    else:
                        obstructions +=1
                        #print ("obstruction at " , oiy, oix, matrix)
                    tests += 1
                    matrix[oiy][oix] = '.'

        # 13213 is too high, 2112 is too low, 1984
        print ( "obstructions" ,obstructions, non_obstructions, tests, not_to_be_testes)
if __name__ == "__main__":
    main()