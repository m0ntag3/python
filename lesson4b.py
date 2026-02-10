# Loops - Sometimes we may need to do a pieces of work repeatedly in such cases we may use loops.
# Defination : A control structure allowing execution of a code block repeatedly until a certain condition is met.
# There are two main types of loops in python i.e: for loop and while loop

# Below is the syntax of a for loop in python:
"""
for variable in range(n):
    # Block of code to be executed
"""
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")
# print("Hello Moses")

for greeting in range(5):
    print("Hello Moses", greeting)

print("===========================")

for number in range(10,20):
    print(number)
# for number in range(10{Starting no.},20{NO. -1[End no.]})

# for even numbers between 50 and 71.
print("============================")
for number in range(50, 71, 2):
    print(number)

print("============================")
# python program printing odd numbers from 100 to 150.
for number in range(101, 150, 2):
    print(number)
print("OOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRR")
for number in range(100,150):
    if number % 2 != 0:
        print(number)
print("========================")
# program printing the multiples of 3 from 201 to 150.
for number in range(201, 149, -3):
    print(number)
print("oooooooooooooooooooooooooorrrrrrrrrrrrrrrrrrrr")
for number in range(201,150,-3):
    if number % 3 == 0:
        print(number)

print("=========================")
#leap years between 2000 and 2024
for number in range(2004, 2023, 4):
    print(number)
print("++++++++++++++++++++++++++")
for number in range (2004, 2023):
    if number % 4 == 0:
        print(number)