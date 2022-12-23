
print ("LIST")
a1 = []
a2 = [ "A", "b","c", "D"]
a3 = [
    [ "A", "b","c", "D"],
    [ "A", "b","c", "D"],
    [ "A", "b","c", "D"]
]
a4 = list()

print ("SET")
b1 = {}
b2 = { "A", "b","c", "D"}


#DIC
c1 = {}
c2 = { "a": 0, "b": 1,"c": 3, "D": 5}
c3 = { "a": { "a": 0, "b": 1,"c": 3, "D": 5} ,
       "b": { "a": 0, "b": 1,"c": 3, "D": 5} ,
}
c1[ "a"] = 1

if "a" in c3:
    print ("A in c3")
print ("a3")

print ("a3-end")
#membership testing

if "A" in a2 and "A" in b2 and "A" in c2:
    print ( "A is everywhere")


for x in b2:
    print (x)
y = range(10)
print ( y )

for x in c2:
    print (x[0] , len(x))


g = [(1,2),(7,2),(7,2),(5,2),(3,2)]
g[1:1] = [(1,3),(7,3)]
for gg in g:
    print (gg[0] , gg[1])

res = [c * 4 for c in [0,1,2,3,18]]
print (res)