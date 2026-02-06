# Dictionary 
# A data type that stores data in terms of key-value pair.
# It is introduced by the use of curly braces {}.
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys.

Phonebook = {
    "Benson" : "2457690894",
    "Mary" : "2541327874" ,
    "Stephen" : "25413142152"
}

# Showing the entire phonebook
print(Phonebook)
print(type(Phonebook))

# Print out Benson's number
print(Phonebook["Benson"])

print('====================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona",  "Argentina"]   
}
# Print Barcelona - the second team he played for
print(player["teams"][1])