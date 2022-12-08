
#n = input ( "Anzahl Kinder" )
#k = input ("Silben: ")

n = 10
k = 3

next = [ (c+1) % n for c in range (n) ]
i = 0# index ist der aktuelle, ausgewählte. nicht der auszuscheidende

while i != next[ i ]:

    for k in range(k):
        i = next[i]

    print ( f"{i} ist ausgeschieden" )
    next[ i ] = next[next[i]]
    i =next[ i ]

print ("Last one: ", i)
