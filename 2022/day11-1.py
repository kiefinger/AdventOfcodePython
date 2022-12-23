import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict
import re


class Monkey:
    def __init__(self, id, startingItems, trueItems, falseItems, op1, op, op2, devidedBy):
        self.id = id
        self.startingItems = startingItems
        self.operation = False
        self.testOperation = False
        self.trueItems = trueItems
        self.falseItems = falseItems
        self.op = op
        self.op1 = op1
        self.op2 = op2
        self.devidedBy = devidedBy
        self.inspected = 0


    def __str__(self):
        return str(self.id) + ' startingItems: ' + str([x for x in self.startingItems])

    def addItem(self, worrylevel):
        self.startingItems.append(worrylevel)


    def inspect(self, monkeyMap):
        for i in range ( len( self.startingItems)):
            item = self.startingItems[i]
            self.inspected +=1
            worrylevel = item
            if self.op2 == "old":
                arg2 = item
            else:
                arg2 = int(self.op2)
            if self.op == '+':
                self.startingItems[i] += arg2
            if self.op == '*':
                self.startingItems[i] *= arg2
            if self.op == '-':
                self.startingItems[i] -= arg2
            if self.op == '/':
                self.startingItems[i] /= arg2

#            self.startingItems[i] //= 3

            #test
            if self.startingItems[i] % self.devidedBy == 0:
                for t in self.trueItems:
                    to = monkeyMap [ t ]
                    to.addItem(self.startingItems[i])
                    #del self.startingItems[i]
            else:
                for t in self.falseItems:
                    to = monkeyMap [ t ]
                    to.addItem(self.startingItems[i])
                    #del self.startingItems[i]

        self.startingItems = []


def  diff (id) :
    tmp = 1

monkeys = []
with open("data/day11-1s.txt") as file:
    lines = file.readlines()

for i in range ( 0, len(lines), 7 ):
    line = lines[i]

    tmp = re.search(r'Monkey (\d):', line)
    if  tmp != None:
        print (line)
        id = tmp.group(1)
        line2 = lines[i+1]
        line3 = lines[i+2]
        line4 = lines[i+3]
        line5 = lines[i+4]
        line6 = lines[i+5]
        # Starting items
        tmp = re.findall(r'(\d+)', line2)
        startingItems = [ int(i) for i in tmp]
        # Operstion
        tmp = re.findall(r'(Operation: )(new)( = )(\w+) ([\*\/\-\+]) (\w+).*', line3)
        a,b,c,d,e,f = tmp[0]

        # Test
        tmp = re.findall(r'(\d+)', line4)
        devidedBy = tmp[0]
        #TRUE
        tmp = re.findall(r'(\d+)', line5)
        trueItems = [ int(i) for i in tmp]
        #FALSE
        tmp = re.findall(r'(\d+)', line6)
        falseItems = [ int(i) for i in tmp]

        m = Monkey(int(id), startingItems, trueItems, falseItems, d, e , f, int(devidedBy))
        monkeys.append(m)

        i +=5

monkeyMap = {}
for i in range(len(monkeys)):
    m = monkeys[i]
    monkeyMap [ m.id ] = m

for round in range(2):
    for i in range(len(monkeys)):
        m = monkeys[i]
        m.inspect(monkeyMap)

    for m in monkeys:
        print (m.id, m.startingItems, m)

listmax = []
for i in range(len(monkeys)):
   m = monkeys[i]
   print (m.inspected)
   listmax.append(m.inspected)

listmax.sort()
print ("MAX2: ", listmax[-2:])

