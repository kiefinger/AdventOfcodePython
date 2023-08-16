import os
dir_path = os.path.dirname ( os.path.realpath(__file__))

print (dir_path)
with open( "data/day02.txt") as file:
    lines = file.readlines()
found = 0
for line in lines:
    args = line.strip().split(" ")
    letter = args[1][0]
    pwd = args[2]
    ids = args[0].split("-");
    x = int( ids[0] )
    y = int( ids[1] )

    c = 0;
    for l in pwd:
        if letter == l:
            c += 1
    if x <= c <= y:
        found +=1

found2 = 0
found3 = 0
for line in lines:
    args = line.strip().split(" ")
    letter = args[1][0]
    pwd = args[2]
    ids = args[0].split("-");
    x = int( ids[0] )
    y = int( ids[1] )
    test =  (( pwd[x-1] == letter and pwd[y-1] != letter) or ( pwd[x-1] != letter and pwd[y-1] == letter))
    if  test:
        found2 += 1


print ( "Found for task 1" , found )
print ( "Found for task 2" ,found2 )
