import os
os.system('cls')

#Tupples can't be changed (immutable)
#Tupples are faster, which is why you would use them for performance, rare that you would have to use them.

tupple_1 = ('John', 'Bob', 'Mary')

#To kinda hack around the fact that they can't be changed

tuple_2 = ('Tina',) #Have to add the comma on single entry

tupple_3 = tupple_1 + tuple_2


print(tupple_3)

print(tupple_1[0:2]) #Prints first two items from tupple (weird, you'd think 0 - 2 would be three items, but nope)
