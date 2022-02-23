songs = [1,2,3,4,5,6,7,8]
print([ x*100 for x in songs ]);

iterate, iterable

for x in range(1,100):
    for x in range(1,100):
        print("haliluyah!!!", x)


someset = { 1,2,3,4,4,4,4,4,4,4,4,2 }
some_other_set = set((1,2,3,4,4,4,4,4,4,1,1,2,3,2,1))

some_tuple  = (1,2,3,3,4,4,23,2,2,34,23,12,34,231)



print(songs[0])

print(someset)
print(some_other_set)

print(some_tuple[0])

print(*(x*120 for x in some_tuple))

matrix = [[1,2], [2,3]]

for x,y in matrix:
    print(' Follow the white rabbit')
    print(x)
    print(y)


def calculator(a,b):
    return a + b

string_number = '100'
print( calculator(1,2))
print( calculator(-1,5))
print( calculator("some text",str(5)))
print( calculator(int(string_number),5))
