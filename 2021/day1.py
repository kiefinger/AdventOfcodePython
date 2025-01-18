
test = [ 199,200,208,210,200,207,240,269,260,263 ]

import os

dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open( "data/day1.txt") as file
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


print (lines)
def part1 ( data):
    inc = 0
    prev = data[0]
    for num in data:
        if num > prev:
            inc+=1
        prev = num

    print ("Number of depth %d " % (inc))

def part2 ( data):
    inc = 0
    prev = -1
    for i in range (2, len(data)):
        if prev == -1:
            prev = data[i-2] +data[i-1] +data[i]
        else:
            sum = data[i-2] +data[i-1] +data[i]
            if ( sum > prev ) :
                inc+=1
            prev = sum
    print ("Number of depth Part 2 %d " % (inc))


part1( lines)

part2( lines)
