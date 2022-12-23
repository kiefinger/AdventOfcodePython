
import re
import copy
from collections import defaultdict
import re

#jtwp: pvnt / slrt
#      pvnt: ptwf + rwrs
#             slrt: 5

# jtwp: pvnt / slrt
# jtwp: pvnt / slrt
#       pvnt: ptwf + rwrs
rv = 0
class Monkey:
    def __init__(self, name, op1, op, op2):
        self.name = name
        self.op1 = op1
        self.op = op
        self.op2 = op2

    def __str__(self):
        return str(self.name + self.op1 + self.op+ self.op2 )


with open("data/day21-1.txt") as file:
    lines = file.readlines()
print (lines)
ops = {}

for line in lines:
    line = line.rstrip()

    ar2 = re.findall(r'(\w+): (\w+) (.) (\w+)', line)
    if not ar2:
        ar1 = re.findall(r'(\w+): (\d+)', line)
        if ar1:
            a,b = ar1[0]
            ops [a] = Monkey( a,b, '=', b)
    else:
        a,b,c,d = ar2[0]
        ops [a] = Monkey( a,b,c,d)

def search (name, s):
    a = ops[name]

#    print ("serach ", a.name, a.op1, a.op2 )

    if a.name == 'nmms':
        tmp = 1

    if a.name == s:
        return 2

    if a.op == "=":
        return 1

    if not a.op1.isnumeric() :
        rc1 = search ( a.op1, s)
    else:
        rc1 = 1



    if not a.op2.isnumeric() :
        rc2 = search ( a.op2, s)
    else:
        rc2 = 1

    return max(rc1,rc2)


def calc (u, name):
    a = u[name]
#    print ("calc", name , a.op1, a.op, a.op2)
    if name == 'nmms':
        tmp = 1
    if a.op == "=":
        return int(a.op1)

    if not a.op1.isnumeric() :
        rc1 = calc (u,a.op1)
    else:
        rc1 = int(a.op1)

    if not a.op2.isnumeric():
        rc2 = calc (u, a.op2)
    else:
        rc2 = int(a.op2)

    if a.op == '+':
        rc = rc1 + rc2
    if a.op == '*':
        rc = rc1 * rc2
    if a.op == '-':
        rc = rc1 - rc2
    if a.op == '/':
        rc = rc1 / rc2

    return rc

def addrevert ( name,left, right):

    a = ops[name]
    if a.op == '+':
        if left:
                return Monkey ( a.op1, name, '-', a.op2 )
        if right:
                return  Monkey ( a.op2, name, '-', a.op1 )
    if a.op == '*':
        if left:
            return  Monkey ( a.op1, name, '/', a.op2 )
        if right:
            return Monkey ( a.op2, name, '/', a.op1 )
    if a.op == '-':
        if left:
            return Monkey ( a.op1, a.op2, '+' , name )
        if right:
            return Monkey ( a.op2, a.op1, '-', name )
    if a.op == '/':
        if left:
            return Monkey ( a.op1,a.op2, '*', name )
        if right:
            return Monkey ( a.op2, a.op1, '/', name )

def calc2 (name):

    if name == "root" or name == "lvvf" or name == "rqgq":
        return rv
    if name == "nmms":
        tmp = 1
    print ("calc", name )

    if name in ops and ops[name].op == '=':
        a = ops[name]
    else:
        #suche in op1 und op2
        for r in ops:
            if ops[r].op1 == name:
                rr = ops[r]
                a = addrevert (r, True, False)
                break

            if ops[r].op2 == name:
                rr = ops[r]
                a = addrevert (r, False, True)
                break

    print ("calc", a.name , a.op1, a.op, a.op2)

    if a.op == "=":
        return int(a.op1)


    if not a.op2.isnumeric():
        rc2 = calc2 ( a.op2)
    else:
        rc2 = int(a.op2)

    if not a.op1.isnumeric() :
        rc1 = calc2 (a.op1)
    else:
        rc1 = int(a.op1)


    if a.op == '+':
        rc = rc1 + rc2
    if a.op == '*':
        rc = rc1 * rc2
    if a.op == '-':
        rc = rc1 - rc2
    if a.op == '/':
        rc = rc1 / rc2

    if rr:
        if rr.op1 == name:
            rr.op1 = str(rc)
        if rr.op2 == name:
            rr.op2 = str(rc)
    ops[name] = Monkey ( name, str(rc), '=', str(rc))
    return rc

opsv = {}



def revert ( name, s, value ):
    a = ops[name]

    if a.name == s:
        return

    # if a.op == "=":
    #     opsv [ name ] = a
    #     return

    if a.op == '+':
        if a.op1 not in opsv :
            opsv [ a.op1] = Monkey ( a.op1, name, '-', a.op2 )
        if a.op2 not in opsv :
            opsv [ a.op2] = Monkey ( a.op2, name, '-', a.op1 )
    if a.op == '*':
        if a.op1 not in opsv :
            opsv [ a.op1] = Monkey ( a.op1, name, '/', a.op2 )
        if a.op2 not in opsv :
            opsv [ a.op2] = Monkey ( a.op2, name, '/', a.op1 )
    if a.op == '-':
        if a.op1 not in opsv :
            opsv [ a.op1] = Monkey ( a.op1, name, '+', a.op2 )
        if a.op2 not in opsv :
            opsv [ a.op2] = Monkey ( a.op2, a.op1, '-', name )
    if a.op == '/':
        if a.op1 not in opsv:
            opsv [ a.op1] = Monkey ( a.op1, name, '*', a.op2 )
        if a.op2 not in opsv :
            opsv [ a.op2] = Monkey ( a.op2, a.op1, '/', name )

    if not a.op1.isnumeric() :
        revert (a.op1, s, value)

    if not a.op2.isnumeric():
        revert (a.op2, s, value)



#copy =s
for key in ops.keys():
    p = ops[key]
    if p.op == '=' and p.name != 'humn':
        opsv[key] = p


def printopv():
    print ( "OPPV Table" )
    for key in opsv.keys():
        p = opsv[key]
        if p.op != '=':
            print (p.name.strip() + ": "+ p.op1.strip()+ " " + p.op.strip()+ " " + p.op2.strip())
        else:
            print (p.name.strip() + ": "+ p.op1.strip())
    print ( "OPPV Table ende" )

#r = ops["root"]
#lf = search ( r.op1, "humn")
#if lf == 2:
#    rv = calc(ops, r.op2)
#    revert ( r.op1,  "humn", rv)
#    opsv [r.op1] = Monkey ( r.op1, str(int(rv)), '=' , str(int(rv)))
#    ops["lvvf"] = Monkey ( "lvvf", str(int(rv)),  '=' , str(int(rv)))
#    ops["root"] = Monkey ( "root", str(int(rv)),  '=' , str(int(rv)))
#    ops["rqgq"] = Monkey ( "rqgq", str(int(rv)),  '=' , str(int(rv)))

#    del ops["humn"]
#    print ( lf, rv, calc2 ("humn"))

#rf = search ( r.op2, "humn")
#if rf == 2:
#    lv = calc(ops, r.op1)
#   rc = revert ( r.op2,  "humn", lv)
#    opsv [r.op2] = Monkey ( r.op2, str(int(rv)), '=' , str(int(rv)))
#    printopv()
#    print ( rf, lv, calc (opsv, "humn"))


ops['humn'] = Monkey ( 'humn', str(3296135418821), '=' , str(3296135418821))
print ("Test")
print ( "Test humn", "root" , calc(ops, "root"))



