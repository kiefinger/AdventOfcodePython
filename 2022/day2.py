import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day02-1.txt") as file:
    lines = file.readlines()

dx = []
for line in lines:
    dxx = line.strip().split(" ")
    dxx[1] = chr( ord( dxx[1])-23 )   # replace xyz by abc
    dx.append(dxx)

print (dx)

a = "A"
b = "B"
c = "C"
worth = { a: 1, b: 2, c: 3}

def f ( x,y ) :
    if  x == y:
       return 3
    if x == a and y == b:
       return 6
    if x == b and y == c:
       return 6
    if x ==c and y == a:
       return 6
    return 0

summe = 0

for draw in dx :
    x,y = ( draw[0], draw[1])
    summe += f ( x,y ) + worth[ y ]
print ( "Exercise 1: ", summe)
# Your puzzle answer was 13052.

summe2 = 0
# handmade map

#     (A) > (C)
#     (C) > (B)
#     (B) > (A)

def g ( x, y ):
    if y == b:
        return x, 3
    if y == a:
        if x == a:
            return c, 0
        if x == b:
            return a, 0
        if x == c:
            return b, 0
    if y == c:
        if x == a:
            return b, 6
        if x == b:
            return c, 6
        if x == c:
            return a, 6
    return "-", -999999

for draw in dx :
     letter, points = g( draw[0], draw[1])
     summe2 += points + worth[ letter]

print ("Exercise 2: ", summe2 )
# Your puzzle answer was 13693.
