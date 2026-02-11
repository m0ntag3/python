# 1. 
def area():
    length = 57
    width = 60
    product = length * width
    print("This is the area of a rectangle", product)

area()

print("==================================")

# 2.
def calculation(x,y):
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y
    print("The evaluations of the two numbers are", sum, difference, product, division)

calculation(99,9)

print("==================================")

# 3.
num =  int(input("Enter number :"))

if num > 0:
    print("This number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("This number is negative")

print("==================================")

# 4.
for number in range(1,15,+1):
    print(number)

print("=====================================")

# 5.
def calculate_squares():
    limit = int(input("Enter a number: "))
    current_num = 1
    while current_num <= limit:
        square = current_num ** 2
        print(f"{current_num} squared is {square}")
        current_num += 1

calculate_squares()