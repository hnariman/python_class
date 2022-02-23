# LISTS & LIST COMPREHENSIONS
# songs = [1,2,3,4,5,6,7,8]
# print([ x*100 for x in songs ]);

# iterate, iterable
## FOR LOOPS
# for x in range(1,100):
#     for x in range(1,100):
#         print("haliluyah!!!", x)
# print(songs[0])

# SET INITIALIZATION AND UNIQ VALUES
# someset = { 1,2,3,4,4,4,4,4,4,4,4,2 }
# some_other_set = set((1,2,3,4,4,4,4,4,4,1,1,2,3,2,1))
# print(someset)
# print(some_other_set)

# TUPLES & GENERATOR FUNCTIONS
# some_tuple  = (1,2,3,3,4,4,23,2,2,34,23,12,34,231)
# print(some_tuple[0])
# print(*(x*120 for x in some_tuple))

# MATRIX OF LISTS (COORDINGATE SYSTEMS)
# matrix = [[1,2], [2,3]]

# for x,y in matrix:
#     print(' Follow the white rabbit')
#     print(x)
#     print(y)


# # FUNCTION ARGUMENTS
# def calculator(a,b):
#     return a + b

# print( calculator(1,2)  )
# print( calculator(-1,5) )
# print( calculator(123/12,5) )

# ## DYNAMIC TYPING AND TYPE CONVERSION IN PYTHON
# string_number = '100'
# print( calculator("some text",str(5)))
# print( calculator(int(string_number),5))
# print("line one")
# print("line two ")
# print("line tree")

# print("line one,\nline two,\nline tree")

# winner = "Orik"
# print(f'and the Oscar goes too')
# print(f'and the Oscar goes too')
# print('and the Oscar goes too', winner)
# print(f'and the Oscar goes too {winner}')

# name="John"
# surname="Malkovic"

# PYTHON F-STRINGS
# print('name: ', name, "surname", surname, 'else')
# print(f'name   :{name}--surname---{surname}')

# IF ELSE ELSE IF
# def drink_test(age):
#     if age < 5:
#         print("drink milk, you!")
#     elif age == 21:
#         print('can drink even Beer, congrats!!')
#     else:
#         print("more than 5 and not 21") 

# drink_test(21)
# drink_test(70)
# drink_test(3)

# def name_check(name):
#     if name is "Matilda":
#         print("Where were you?!!!")
#     else:
#         print(f"Greetings stranger named {name}")


# name_check("Matilda")
# name_check("Naomi")


## DANGEROUSLY INFINITE LOOP
# i=14
# while True:
#     i+=1
#     print(f'infinity... {i+4} ')

# time complexity of algorithm O(n)
# for i in range(1,100):

# time complexity of algorithm O(n**n) -> log(n)
# for i in range(1,100):
#     for n in range(1,100):
# 10.000 iterations

# Python ranges
for index in range(1,40, 5):
    print(index)









