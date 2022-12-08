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

# A for Rock, B Paper, C Scissors
#Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# (2 because you chose Paper + 6 because you won)
#     (A) > (C)
#     (C) > (B)
#     (B) > (A).
#     both players choose the same shape, the round instead ends in a draw.

def f ( x,y ) :
    if  x == y:
        return 3
    if x == a:
        if y == c :
            return 0
        else:
            return 6
    if x == b:
        if y == a:
            return 0
        else:
            return 6
    if x ==c:
        if y == b:
            return 0
        else:
            return 6
    return 999999

summe = 0

for draw in dx :
    x,y = ( draw[0], draw[1])
    summe += f ( x,y ) + worth[ y ]
print ( "Exercise 1: ", summe)
# Your puzzle answer was 13052.

summe2 = 0
# handmade map
draws2 = {
    ("A", "A"):  ["C", 0 + 3],
    ("A", "B"):  ["A", 3 + 1],
    ("A", "C"):  ["B", 6 + 2],
    ("B", "A"):  ["A", 0 + 1],
    ("B", "B"):  ["B", 3 + 2],
    ("B", "C"):  ["C", 6 + 3],
    ("C", "A"):  ["B", 0 + 2],
    ("C", "B"):  ["C", 3 + 3],
    ("C", "C"):  ["A", 6 + 1]
}

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
#     print ( draw[0], draw[1], letter, points, worth[ letter] )
     summe2 += points + worth[ letter]

print ("Exercise 2: ", summe2 )
# Your puzzle answer was 13693.
