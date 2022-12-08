import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open("data/day01-1.txt") as file:
    lines = file.readlines()

totalmax = 0
currenttotal = 0
m = []
print (len(lines))
for i in range(len(lines)):
    line = lines[i].strip()
    currenttotal += int(line) if len(line) > 0 else 0
    if (len (line)) == 0  :
       if currenttotal> totalmax:
           totalmax = currenttotal
           print ( "New max: ", totalmax)
       m.append(currenttotal)
       currenttotal = 0

m.sort()
print ( "The highest 3", m[-3:] , "= " , sum ( m[-3:]))