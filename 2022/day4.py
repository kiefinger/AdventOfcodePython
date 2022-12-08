import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day05-1.txt") as file:
    lines = file.readlines()

par = []
n = 0
overlap = 0
for line in lines:
    par = line.strip().split((","))
    lpar = [ int(i) for i in par[0].split("-")]
    rpar = [ int(i) for i in par[1].split("-")]

    left = set(range (lpar[0], lpar[1]+1))
    right = set(range (rpar[0], rpar[1]+1))

    if left & right == left:
        n += 1

    elif right & left == right:
        n += 1
    if len(left & right)> 0 :
        overlap += 1

print ( "Ergebnis 1: ", n)
print ( "Ergebnis 2: ", overlap)
