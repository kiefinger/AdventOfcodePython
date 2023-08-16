

import os

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day2.txt") as file:
    lines = file.readlines()

x = 0
y = 0
aim = 0;
#down X increases your aim by X units.
#up X decreases your aim by X units.
#forward X does two things:
#It increases your horizontal position by X units.
#It increases your depth by your aim multiplied by X.

for l in lines:
    a, b = l.strip().split( " ")
    if ( a == "forward"):
        x += int(b)
        y += (int(b) * aim)
    if ( a == "down"):
#        y += int(b)
        aim += int(b)
    if ( a == "up"):
#        y -= int(b)
        aim -= int(b)





result = x*y
print ("restul" , result )