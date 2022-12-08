import os
import re
import copy

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
ns = 3

with open("data/day05-1s.txt") as file:
    lines = file.readlines()
stack = []
for i in range ( ns+1) :
    stack.append ([])

#sl = []
#ml = []
# for line in lines:
#     line = line.rstrip()
#
#     print ( line)
#     if line.find( '[' ) > -1:
#         sl.append (line)
#     if line.startswith(" 1 "):
#         numberline = line
#     if line.startswith("move"):
#         ml.append ( line)

numberline = [ line.rstrip() for line in lines if line.startswith(' 1 ')]
sl = [ line.rstrip() for line in lines if line.find( '[' ) > -1]
ml = [ line.rstrip() for line in lines if line.startswith("move")]

print ( "numberline" , numberline)
print (ml )

print ( sl)
sl.reverse()
print ( sl)

for sli in sl:
    for i in range ( ns ):
        if ( len(sli)> i*4+1) and sli[i*4+1] != ' ':
            stack[i+1].append (sli[i*4+1])

# with regex
#for sli in sl:
#    yyy = re.findall(r'(\[.\]|    )', sli)
#    for i in range (ns ):
#        if yyy[i][1] != ' ':
#            stack[i+1].append (yyy[i][1])
#

print  ("Stack", stack )

stack2 = copy.deepcopy(stack)

for mli in ml:
    print ( mli )
    mlid = re.findall(r'\d+', mli)
    c = int(mlid[0])
    f = int(mlid[1])
    t = int(mlid[2])
    print ( "cft", c, f, t )

    for e in range ( c ):
        x = stack[f].pop()
        stack[t].append( x )

    print (stack)

print ( "Result 1:")
result = [ stack[e].pop() for e in range( 1, ns +1)]
print ( "".join(result))
#Ergebnis s1 = LJSVLTWQM


print  ("Stack", stack2 )
tmp = []
for mli in ml:
    print ( mli )
    c = int( mli[5:7])
    f = int( mli[12:14])
    t = int(mli[17:])
    print ( "cft", c, f, t )

    for e in range ( c ):
        x = stack2[f].pop()
        tmp.append( x )
    for e in range ( c ):
        x = tmp.pop()
        stack2[t].append( x )

    print (stack2)

print ( "Result 2:")
result = [ stack2[e].pop() for e in range( 1, ns +1)]
print ( "".join(result))