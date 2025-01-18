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

def main():
    with open("data/day06.txt") as file:
        rulesComming = True
        i =0
        for line in file.read().splitlines():
            matrix.append ( list ( line))
            if  line.find('^') > 0:
                starty = i
                startx = line.find('^')

            i+=1

        print ( starty,startx, len(matrix), len(matrix[0]), matrix )
        obstructions = 0
        non_obstructions = 0;
        tests = 0
        not_to_be_testes = 0
        for oiy in range ( len(matrix)):
            for oix in range ( len(matrix[0])):
                if matrix[oiy][oix]!='#' and matrix[oiy][oix]!='^':
                    #print("check point", y, x, matrix)

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

                        if nexty < 0 or nexty >= len(matrix):
                            break
                        if nextx < 0 or nextx >= len(matrix[0]):
                            break
                        #print("check", y, x, matrix)
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
                else:
                    #print ( "not to be testeed", oiy, oix)
                    not_to_be_testes +=1

        # 13213 is too high, 2112 is too low
        print ( "obstructions" ,obstructions, non_obstructions, tests, not_to_be_testes)
if __name__ == "__main__":
    main()