import re

str1 = "Monkey 0:"
str2 = "Starting items: 79, 98"
str3 = "Operation: new = old * 19"
str4 = "Test: divisible by 23"
str5 = "If true: throw to monkey 2"
str6 = "If false: throw to monkey 3"

#tmp = re.findall(r'(Operation: )(new)( = )(\s) ([\*\/\-\+]) (\d+).*', str3)
tmp = re.findall(r'(Operation: )(new)( = )(\w+) ([\*\/\-\+]) (\d+).*', str3)
print ( tmp )
tmp2 = [0]
a,b,c,d,e,f = tmp[0]

str1 = "[1,1,3,1,1]"
str1 = "[[2],1,1,3,1,1]"
tmp = re.findall(r'(\[.*\])', str1)
for t in tmp:
    print (t)
    tmp = re.findall(r'(\d+)|(\[.*\])+', t[1:])
    for t in tmp :
       print (t)
