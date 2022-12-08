import os

dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open( "data/matrix1.txt") as file:
    lines = file.readlines()
#    array = [  line.rstrip().split(',"') for line in lines]
array = []
for l in lines:
    array.append ( l.strip().replace(' ','').split(',') )

v = []
#prblocint (array)
for x in  range(len(array)):
    for y in range(len(array[x])):
        if  x < len(array)-1:
#           print ( array[x][y], array[x+1][y] )
#           print (tuple( [array[x][y], array[x+1][y] ]))
            v.append( tuple( [array[x][y], array[x+1][y] ] ))
        if  y < len(array[x])-1:
            v.append( tuple( [ array[x][y], array[x][y+1] ]))
print (v)