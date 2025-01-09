
numbers = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263];

inc = 0;
last = numbers[0]
for n in numbers :
    if ( n > last ) :
        print ( str(n) + " > " + str(last))
        inc = inc+1;
    last = n;

print ( inc )
