# 1.
for numbers in range(2000,2025):
    print(numbers)

print("++++++++++++++++++++++++++")

# 2.
Colors = ["Blue","Green","Red", "Pink","Black"]
for Color in Colors:
    print(Color)

print("++++++++++++++++++++++++++")
# 3.
number = 20
while number >= 1:
    print(number)
    number= number - 1

print("++++++++++++++++++++++++++")

# python functions with and without parameters.
    # Function - Code block that operates when called.
                        # Types of functions:
                        # 1. Bulit-in functions; print(), input(), range()
                        # 2. User- defined functions; 
                        # def greet(name):
                        #     return f"Hello, {name}!"

                        #     print(greet("Alice"))
                        # 3. Lambda/anonymuos functions; small, one-line functions defined without a name
                        # 4. method functions; functions that belong to an object or a class.

        # Python functions without parameters - Used for tasks that stay constant.(Self-reliant)
            # Syntax - Has definition(def), function, parenthesis that are left blank ()and a colon(:) at the end.
            # Can be used to display messages i.e Welcome and Static timelapse generation.

def greet_person():
        print("Good Morning, you are welcome")

greet_person()

        # Python functions with parameters - Hold place for data to be passed into function.
            # Syntax - Variables are defined in parenthesis.
            # Arguments - Values to be passed into the function.

print("++++++++++++++++++++++++++")

def personal_greeting(name):
     print(f"Good Morning, {name}! you are welcome")

personal_greeting("Collins")