# Python list (Sequence Type)
# A list in python is a collection of items ordered  in a certain way.
# A list is introduced by the use of the square brackets []
# The items of the list are stored inside of indexes. NOTE: In programming we start counting from index zero(0). E.g. BMW, Mercedes Benz, Audi.
# A list is mutable i.e. the contents of the list can be changed.

cars = ["BMW", "Mercedes Benz", "Bugatti", "Mc Laren", "Citreon", "Land cruiser", "Pagani"]

print(cars)
print(type(cars))

# Accessing items of a list.
print(cars[2])
print("the car on index four is", cars[4])
print("the car on index zero is", cars[0])

# List slicing. 
# This is coming up/creating a list from a given index/ figure.
print(cars[4:])

# Printing from index zero to index three
print(cars[:4])

# Printing from Bugatti to Citreon
print(cars[2:5])

# List mutability.
# We use the function append to add items to a list.
cars.append("Chevloret")
print(cars)
cars.append("Dodge")
print(cars)

# We use the pop function to remove an item at the end of the list.
cars.pop()
print(cars)

# We use an index to add(replace) items of the list.
cars[5] = 'Pajero'
print(cars)

# We use the sort function to sort items on the list in alphabetical order.
cars.sort(reverse= True)
print(cars)

# We use del., .pop, .remove to delete items on a list.
del cars[4]
print(cars)

cars.pop(3)
print(cars)

cars.remove("BMW")
print(cars)