import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict
import re

def main():

    monkeys = []
    monkeyMap = {}
    divisorProduct = 1

    with open("data/day11-1.txt") as file:
        lines = file.readlines()

    for i in range ( 0, len(lines), 7 ):

        id = int(lines[i][7])
        startingItems = [ int(i) for i in re.findall(r'(\d+)', lines[i+1])]
        operator   = lines[i+2][23]
        operand    = lines[i+2][25:].strip()
        devidedBy  = int(lines[i+3][21:])
        trueItems  = int(lines[i+4][29:])
        falseItems = int(lines[i+5][30:])

        m = Monkey(id, startingItems, trueItems, falseItems, operator , operand, int(devidedBy))
        monkeys.append(m)
        monkeyMap [ m.id ] = m
        divisorProduct *= devidedBy


    print ( "divisorProduct", divisorProduct)

    #inspect
    for r in range(10000):
        for i in range(len(monkeys)):
            m = monkeys[i]
            m.inspect(monkeyMap, divisorProduct)

    #calc max
    listmax = [ m.inspected for m in monkeys]
    listmax.sort()
    print ("MAX2: ", listmax[-2:])


class Monkey:
    def __init__(self, id, startingItems, trueItems, falseItems, op, op2, devidedBy):
        self.id = id
        self.startingItems = startingItems
        self.operation = False
        self.testOperation = False
        self.trueItems = trueItems
        self.falseItems = falseItems
        self.op = op
        self.op2 = op2
        self.devidedBy = devidedBy
        self.inspected = 0

    def __str__(self):
        return str(self.id) + ' startingItem: ' + str([x for x in self.startingItems])

    def addItem(self, startingItem):
        self.startingItems.append(startingItem)

    def inspect(self, monkeyMap, divisorProduct):
        for i in range ( len( self.startingItems)):
            self.inspected +=1
            worrylevel = self.startingItems[i]
            if self.op2 == "old":
                arg2 = worrylevel
            else:
                arg2 = int(self.op2)
            if self.op == '+':
                worrylevel += arg2
            if self.op == '*':
                if arg2 =="old":
                    worrylevel *= arg2
                else:
                    worrylevel *= arg2
            if self.op == '-':
                worrylevel -= arg2
            if self.op == '/':
                worrylevel /= arg2

            worrylevel = worrylevel % divisorProduct

            if worrylevel % self.devidedBy == 0:
                monkeyMap [ self.trueItems ].addItem(worrylevel)
            else:
                monkeyMap [ self.falseItems ].addItem(worrylevel)

        self.startingItems = []


main()
# correct MAX2:  [156713, 164077]
