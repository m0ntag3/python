# A python for loop can be used to iterate through a list, tuple, string or even a dictionary.

name = "Collins"

for letter in name:
    if letter == "o":
        print("This is letter o")
    else:
        print(letter)
# NOTE: IF goes hand in hand with ELSE.

print("=====================")
#Below is a list of several counties
counties = ("Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu")
print(counties)

for county in counties:
    print(county)

print("++++++++++++++++++++++")
counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu", "Kisumu")
for county in counties:
    if "Kisumu" in counties:
        print("County found")
        break
    else:
        print("County not found")

player = {
    "name" : "Mbappe",
    "age" : 23,
    "teams" : ["Monaco","PSG", "Real Madrid"],
    "nationality" : "French"
}
for key in player:
    print(key)

print("+++++++++++++++++++++++")
for values in player:
    print(player[values])

print("++++++++++++++++++++")
for team in player["teams"]:
    print([team])