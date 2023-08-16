import logging
import os
import unittest
# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/4
# You need to use the binary numbers in the diagnostic report to generate two new binary
# numbers (called the gamma rate and the epsilon rate).
#
# Task 1:
# Find the most common bit in a column of data


dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day3s.txt") as file:
    lines = file.readlines()
nLines = len(lines)
matrix = []
for l in lines:
    matrix.append ([int(c) for c in list(l.strip())])

print (matrix)
cols = len(matrix[0])
gammaCounter = [0 for c in range (cols)]

# First we sum up the "1" of each column in the source data and collection this data in a gammaCounter array.
# Then  we build a integer using binary operations to set a bit if the relevant column is the most common value 1 or 0
# we do the same for the least common value and collect this data in a epsilonbin.

for row in matrix:
    for i in range(cols):
        gammaCounter[i] +=row[i]
#    n += 1
print ( gammaCounter)
print ( "n:", nLines)
gammabin = 0
epsilonbin = 0
print (range(cols))
for i in range(cols):
    if gammaCounter[i] > nLines/2 :
        gammabin = gammabin | 2**(cols-i-1)
        logging.debug( "G:" , gammabin)
    if gammaCounter[i] < nLines/2 :
        epsilonbin = epsilonbin | 2**(cols-i-1)
        logging.debug( "E:" , epsilonbin)
print ("Result = ", gammabin * epsilonbin )


# Task 2
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen
# generator rating by the CO2 scrubber rating.
# Both values are located using a similar process that involves filtering out values until only one remains.

# Calculate OxigenRate
oxigenFinderArray = [1 for c in range (nLines)]

# das würde auch gehen. Abe nicht fertig getestet.
oxigenFinderMap = { 1: True for c in range (nLines) }

relevantCols = nLines
# find lines, that fit to the most common value. delte all other lines.
# insted of deleting these lines I use a oxigenFinderArray and mark every line as 0=deleted
for i in range(cols):
    if gammaCounter[i] >= relevantCols/2:
        for y in range(nLines):
            if matrix[y][i] == 0:
                if oxigenFinderArray[y] == 1:
                    oxigenFinderArray[y] = 0
        print (oxigenFinderArray )
    else:
        for y in range(nLines):
            if matrix[y][i] == 1:
                if oxigenFinderArray[y] == 1:
                    oxigenFinderArray[y] = 0
    # if there is only one line left, stop her
    summe = sum (oxigenFinderArray)
    if ( summe == 1):
        break
    # recount to find the most common value based on the rows that are left (not deleted) (only if oxigenFinderArray[rowIndex]==1)
    gammaCounter = [0 for c in range (cols)]
    for rowIndex in range(len(matrix)):
        for ii in range(cols):
            if oxigenFinderArray[rowIndex]==1:
                gammaCounter[ii] += matrix[rowIndex][ii]
    relevantCols =  sum (oxigenFinderArray)

# find the index of oxigenFinderArray where the value is 1
for i in range (nLines):
    if oxigenFinderArray[i]==1:
        oxigenIndex = i
        break
oxigenRate = 0
for col in range(cols):
    if matrix[oxigenIndex][col] == 1:
      oxigenRate = oxigenRate | 2**(cols-col-1)

# Calculate Scrubber Rate

for row in matrix:
    for i in range(cols):
        gammaCounter[i] +=row[i]
relevantCols = nLines
oxigenFinderArray = [1 for c in range (nLines)]

for i in range(cols):
    if gammaCounter[i] < relevantCols/2:
        for y in range(nLines):
            if matrix[y][i] == 0:
                if oxigenFinderArray[y] == 1:
                    print ("Delete line: " , y)
                    oxigenFinderArray[y] = 0
        print (oxigenFinderArray )
    else:
        for y in range(nLines):
            if matrix[y][i] == 1:
                if oxigenFinderArray[y] == 1:
                    print ("Delete line: " , y)
                    oxigenFinderArray[y] = 0
    # if there is only one line left, stop her
    summe = sum (oxigenFinderArray)
    print (oxigenFinderArray )
    if ( summe == 1):
        break
    # recount
    gammaCounter = [0 for c in range (cols)]
    for rowIndex in range(len(matrix)):
        for ii in range(cols):
            if oxigenFinderArray[rowIndex]==1:
                gammaCounter[ii] += matrix[rowIndex][ii]
    relevantCols =  sum (oxigenFinderArray)

for i in range (nLines):
    if oxigenFinderArray[i]==1:
        oxigenIndex = i
        break
scrubberRate = 0
for col in range(cols):
    if matrix[oxigenIndex][col] == 1:
        scrubberRate = scrubberRate | 2**(cols-col-1)


print (oxigenRate)
print (scrubberRate)
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen
# generator rating by the CO2 scrubber rating.

print ( "resutl = ",  oxigenRate * scrubberRate)

if __name__ == '__main__':
    unittest.main()