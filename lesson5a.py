#  PYTHON FUNCTIONS
# A block of code/statement that performs a given task/action. Can be reused throghout the program to perform different tasks.
# Defined using the def keyword(def).
# There are two main types i.e:
# 1.In-built functions-> Come preinstalled with the interpreter i.e print(), pop(), range(), append() e.t.c
# 2. User-defined funtions=> created by the programmer to solve a given task .
# To define a function you need to give it a name  followed by parenthesis.
# For the function,it is usually indented and invoke a function we use the function name.

def greetings():
    print("Hello,how are you?")

# We call the function by using its name
greetings()

print("=====================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is",sum)

addition()

print("+++++++++++++++++++++++++")

# Reason for num1 being used as different no.s is because each function has the num1s as its local value.

# A function able to multiply three values
def product():
    num1 = 34
    num2 = 4
    num3 = 5
    multiply = num1 * num2 * num3
    print("The product of the numbers is", multiply)

product()

print("==============================")

def divide():
    print("This is calculation",[y])
    number1 = int(input("Enter first number :"))
    number2 = int(input("Enter second number : "))
    quotient = number1 / number2
    print("The answer is", quotient)
    print("-------")

for y in range(1,4):
    divide()
    