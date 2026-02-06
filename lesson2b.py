# Tuple
# An immutable type of list(cannot be changed)
# To Introduce it you use parenthesis().

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties)
print(type(counties))

# Slicing of tuples.
print(counties[3:])

# Accessing items of a tuple by use of indices.
print(counties[5])

# NOTE: Below will generate an error.
# Attribute error.
counties.append ("Machakos")
print(counties)
