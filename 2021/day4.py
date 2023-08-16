import os
import re

class Card :

    def __init__(self, c):
        self.card = c
        self.marked = [[0 for i in range(5)] for j in range(5)]
    def toString(self):
        return [[str(self.card[i][e]) for i in range(5)] for e in range(5)]
    def toStringMarked(self):
        return [[str(self.marked[i][e]) for i in range(5)] for e in range(5)]
    def mark(self,x,y):
        self.marked[x,y] = 1
    def mark(self,number):
        for i in range(5):
            for e in range(5):
                if self.card[i][e]==number:
                    self.marked[i][e]=1

    def checkRow(self, i ):
        return sum(self.marked[i]) == 5
    def checkCol ( self, y):
        s = self.marked[0][y]+self.marked[1][y]+self.marked[2][y]+self.marked[3][y]+self.marked[4][y]
        return s == 5 ;
    def checkBingo ( self ):
        for i in range(5):
            if self.checkRow(i)==True:
                return True
        for i in range(5):
            if self.checkCol(i)==True:
                return True
        return False
    def sumUnmarked( self ) :
        self.sum = 0
        for i in range(5):
            for e in range(5):
                if self.marked[i][e]==0:
                    self.sum += self.card[i][e]
        return self.sum

cols = 12

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day4.txt") as file:
    lines = file.readlines()

numbersline = lines.pop(0)

numbers = [int(c) for c in numbersline.strip().split(",")]
print ( numbers )
nCards =0
cards = []
card = [[0 for i in range(5)] for j in range(5)]

i = 0
for  line in lines:
    line = line.strip()
    line = re.sub(' +', ' ', line)
    if len(line)> 0:
        print ( line.strip().split(" ") )
        card[i] = [int(c) for c in line.strip().split(" ")]
        i += 1
    if ( i==5 ):
        cards.append(card.copy())
        card = [[0 for i in range(5)] for j in range(5)]
        i=0

print (cards)
nCards = len(cards)
bingoIndex = [0 for j in range(nCards)]
lastBoardIndex = -1


cardsc = []
for c in cards:
    cc = Card(c)
    cardsc.append( cc)
for c in cardsc:
    print (c.toString())

def markNumber( number ):
    for c in cardsc:
        c.mark(number)
# only check
def checkBingo(  ):
    firstboardIndex = -1
    for boardIndex in range (len((cardsc))):
        if bingoIndex[boardIndex] == 0:
            if cardsc[boardIndex].checkBingo() == 1:
                bingoIndex[boardIndex] = 1
                print ( "Binge at board" , boardIndex )
                firstboardIndex =  boardIndex
 #               global.lastBoardIndex = boardIndex
    return firstboardIndex

winnderBoard = -1
bingos = 0
for number in numbers:
    print (number)
    markNumber(number)
    boardIndex =checkBingo()
    if boardIndex>-1 :
        if winnderBoard <0 :
            winnderBoard = boardIndex
            print ("Bingo at board:" , boardIndex )
            print ( "Number: " , number)

            print ( "Summme Unmarked" , cardsc[boardIndex].sumUnmarked() )

            print ( "Result " ,  number * cardsc[boardIndex].sumUnmarked() )

            print ("Winner Board", cardsc[boardIndex].toString())
            print ("Winner Board", cardsc[boardIndex].toStringMarked())
        bingos += 1
        if sum(bingoIndex) == nCards:
            print ("Last Bingo at board:" , boardIndex )
            print ( "Summme Unmarked" , cardsc[boardIndex].sumUnmarked() )
            print ( "Result 2" ,  number * cardsc[boardIndex].sumUnmarked() )
            break;


#last index is keine globale variabel

