import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day03-1.txt") as file:
    lines = file.readlines()
#    lines = [line.rstrip('\n') for line in file]

def calcvalue(letter):
    return ord(letter)-96 if ord(letter) >= 97 else ord(letter )-65+27

#task 1
rc = 0

for line in lines:
    line = line.strip()
    l = len(line)//2

    left = line[0:l]
    right = line[l:]
    for i in range(l):
        if right.find(left[i]) > -1:
            rc += calcvalue(left[i])
            break
print ("Exercise 1: ", rc )

print ("Exercise 1 mit sets" )
rc = 0
for line in lines:
    line = line.strip()
    l = len(line)//2

    common = set(line[0:l]) & set(line[l:])
    for letter in common:
        rc += calcvalue(letter)

print ("Exercise 1 mit sets: ", rc)

print ("Exercise 2 ")
rc = 0
for i in range ( 0, len(lines)-2, 3):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()

    old = []
    for i in range(len(line1)):
        if line2.find(line1[i]) > -1 and line1[i] not in old:
             if line3.find(line1[i]) > -1:
                rc += calcvalue(line1[i])
                old.append(line1[i] )

print ("Exercise 2: ", rc )

print ("Exercise 2 mit set")
rc = 0
for i in range ( 0, len(lines)-2, 3):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()

    common = set(line1) & set(line2) & set(line3)
    for letter in common:
        rc += calcvalue(letter)

print ("Exercise 2 mit set: ", rc )
# Your puzzle answer was 13693.
