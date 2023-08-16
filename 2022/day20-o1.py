n1000 = n2000 = n3000 = 0
sequence = []

encrypted = open("data/day20-1.txt").read().strip().split("\n") # prod
for i in range(len(encrypted)):
    line = int(encrypted[i])
    sequence.append(line)

lens = len(sequence)
index = [i for i in range(lens)]

for i, number in enumerate(sequence):
    value = sequence[i]
    position = [j for j, x in enumerate(index) if x == i][0]
    index.pop(position)
    moveto = (position + value) % (lens - 1)
    index.insert(moveto, i)

last = [sequence[i] for i in index]
poszero = [i for i, x in enumerate(last) if x == 0][0]
n1000 = last[(1000 + poszero) % lens]
n2000 = last[(2000 + poszero) % lens]
n3000 = last[(3000 + poszero) % lens]

print("answer1 ", n1000+n2000+n3000)