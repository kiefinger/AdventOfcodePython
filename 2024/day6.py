from collections import defaultdict

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
                y = i
                x = line.find('^')

            i+=1
        starty = y
        startx = x

        print ( y,x, len(matrix), len(matrix[0]), matrix )
        move_index = 0
        visits = 0
        while True:
            if matrix[y][x] != 'X':
                visits +=1
            matrix[y][x] = 'X'
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

        print (visits)

if __name__ == "__main__":
    main()