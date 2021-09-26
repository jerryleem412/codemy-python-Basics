import os
os.system('cls')


#Dictionary, called hashes in other languages


fav_pizza = {
    "John": "Pepperoni", 
    "Bob": "Mushroom", 
    "Tina": "Supreme"
}

print(fav_pizza)
print(fav_pizza["John"])

#Delete item
del fav_pizza["John"]
print(fav_pizza)

#Change
fav_pizza["Bob"] = "Ham"
print(fav_pizza)

#Add
fav_pizza.update({"Tim": "Green Peppers"})
print(fav_pizza)