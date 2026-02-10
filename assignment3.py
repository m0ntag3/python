Gross_Salary = float(input("Enter Salary, "))
if Gross_Salary <= 5999:
    print("Monthly Contribution", 150.00)
elif Gross_Salary >= 6000 and Gross_Salary <= 7999:
    print("Monthly Contribution", 300.00)
elif Gross_Salary >= 8000 and Gross_Salary <= 11999:
    print("Monthly Contribution", 400.00)
elif Gross_Salary >= 12000 and Gross_Salary <= 14999:
    print("Monthly Contribution", 500.00)
elif Gross_Salary >= 15000 and Gross_Salary <= 19999:
    print("Monthly Contribution", 600.00)
elif Gross_Salary >= 20000 and Gross_Salary <= 24999:
    print("Monthly Contribution", 750.00)
elif Gross_Salary >= 25000 and Gross_Salary <= 29999:
    print("Monthly Contribution", 850.00)
elif Gross_Salary >=30000 and Gross_Salary <= 49999:
    print("Monthly Contribution", 1000.00)
elif Gross_Salary >= 50000 and Gross_Salary <= 99999:
    print("Monthly Contribution", 1500.00)
else:
    print("Monthly Contribution", 2000.00)

number = 1000000
formatted_number = format(number, ",")
print(formatted_number) 

format(number, ",")

    # Looping
    # 1. For loop
    # 2. While Loop

# For Loop - used to iterate over a sequence.(For every item in collection do "this")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}s!")
    # Can either use: i. range(n)
    #                ii. sequence

    # Range()
    # To print 0 through 4:
for i in range(5):
    print(f"Iteration{i}")

# While loop - used to keep code running as long as a specific condition is True.
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # Crucial! Without this, you get an infinite loop.
print("Blast off!")  

# Control statements;
# 1. Break - Stops loop immediately
# 2. continue - Skip the rest of the current iteration and jumps to the next.
# 3. else - run a block of code once the loop finishes normally.