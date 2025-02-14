
insts = []
with open("data/day10-1.txt") as file:
    for line in file.readlines():
        line = line.strip()
        inst = line.rstrip().split()
        insts.append(inst)

X = 1
circ = 0
crt = []

for i in range(6):
    crt.append ( [ 0 for e in range ( 40) ])

def printCrt():
    for i in range(6):
        str = ""
        for e in range(40):
            if crt[i][e] == 1:
                str += chr( crt[i][e]+48)
            else:
                str += " "
        print ("'", str, "'")

def checkCrt(circ, X):
    global crt
    circ -= 1
    row = (circ // 40) % 6
    col = circ % 40
    if X-1 == col:
        crt[row][col] = 1
    if X == col:
        crt[row][col] = 1
    if X+1 == col:
        crt[row][col] = 1

#main
for inst in insts:
    op = inst[0]

    if op == "noop":
        circ += 1
        checkCrt (circ, X)

    if op == "addx":
        circ += 1
        checkCrt (circ, X)
        circ += 1
        checkCrt (circ, X)
        X += int(inst[1])

printCrt()
