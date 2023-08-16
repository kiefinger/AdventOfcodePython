import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day01.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

print (lines)
#
# for i in lines:
#     for e in lines :
#             if i+e == 2020 :
#                 print (i,e, i*e)
#
for i in lines:
     for e in lines :
         for x in lines:
             if i+e+x == 2020 :
                 print (i,e,x, i*e*x)


for i in range ( len(lines) ):
    for e in range (i, len(lines)):
        if lines[i] + lines[e] == 2020 :
            print (lines[i] , lines[e] , lines[i] * lines[e] )

for i in range ( len(lines) ):
    for e in range (i+1, len(lines)):
        for x in range (e+1, len(lines)):
            if lines[i] + lines[e]+ lines[x] == 2020 :
                print (lines[i] , lines[e] , lines[x], lines[i] * lines[e] *lines[x])
