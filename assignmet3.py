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