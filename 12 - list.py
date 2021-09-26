import os
os.system('cls')

#Lists

#List can be changed (Mutable)
first_names = ["John", "Bob", "Mary"]
first_names[1] = "Tina"  #Udate an item
del first_names[0] #Delate items
print(first_names)

#add different types to list
test = ["jack", "Tony", "Jerry"]
test[0] = first_names
print(test)

#appedn things to the list
test.append("Greg")
print(test)

#Length of list
print(len(test))