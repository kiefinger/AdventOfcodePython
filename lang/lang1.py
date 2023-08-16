
a = "abc"


print (type(a))
print ( isinstance(a, str ))

b = [ "A", "b","c", "D"]
print (b)
pointer = b[0]
print (b)
b[0] = "X"
print (b)
print (pointer)


c = [
[ "A", "b","c", "D"],
[ "A", "b","c", "D"],
[ "A", "b","c", "D"]
]
for x in c:
    print (x[0] , len(x))

d = ( 1,2,3)
for y in d:
    print ( y)
e = set()
e.add("a")
e.add("b")

g = [(1,2),(7,2),(7,2),(5,2),(3,2)]
g[1:1] = [(1,3),(7,3)]
for gg in g:
   print (gg[0] , gg[1])

a = set ("abcdaa")
print ( a)

for circ in range (800):
    row = (circ // 40) % 6
    print (circ, row)
