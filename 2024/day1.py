import os

dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day01.txt") as file:
    lines = file.readlines()

left = []
right = []
for line in lines:
   arg1, arg2 = line.strip().split()
   left.append ( int(arg1) )
   right.append ( int(arg2) )
left.sort();
right.sort();

def part1 ( data):
    diff = 0
    h = len(left);
    for i in range(h):
        diff += abs((right[i] - left[i]))
        print ( "left %d, right %d, " % (left[i], right[i]))

    print ("Number of diff= %d " % (diff))

def part2 ( data):
    inc = 0
    prev = -1
    for i in range (len(left)):
        found = 0;
        for e in range (len(right)):
            if left[i] == right[e]:
                found += 1
        inc += (left[i] * found)
    print ("Number of depth Part 2 %d " % (inc))


part1( lines)

part2( lines)
