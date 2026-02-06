# A python program able to determine whether a number entered is an odd or even number.
# numeral = int(input("Enter your numeral "))
# if numeral % 2 == 0:
#     print("This numeral is even")
# else:
#     print("This numeral is odd")

# A python program able to determine whether a peron is able to donate blood based on their weight and age. If the age is above 18 and weight above 50kgs the student is able to donate,else not possible.
age = int(input("Enter age "))
weight = float(input("Enter weight "))
if age >=18 and weight > 50.0:
    print("Able to donate blood")
else:
    print("Unable to donate blood")