# 1. Simple interest
def simple_interest():
    p = int(input("Enter principle: "))
    r = int(input("Enter rate: "))
    t = int(input("Enter time: "))
    interest = p * r * t / 100
    print("The simple interest is:", interest)

simple_interest()

# Body Mass Index
def body_mass_index():
    weight = int(input("Enter weight: "))
    height = int(input("Enter height: "))
    index = weight / (height ** 2)
    print("The Body Mass Index is:", index)

body_mass_index()