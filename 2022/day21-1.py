import re
import copy
from collections import defaultdict
import re


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

def calc (name):
    a = ops[name]

    if a.op == "=":
        return int(a.op1)

    if not a.op1.isnumeric() :
        rc1 = calc (a.op1)
    else:
        rc1 = int(a.op1)

    if not a.op2.isnumeric():
        rc2 = calc ( a.op2)
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


print ( calc ("root"))




