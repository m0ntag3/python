# Nested If statement
# An If statement contained inside another If statement.

age = 21
weight = 55
blood_group =  "B"

if age > 15:
    if weight > 50:
        if blood_group =="A":
            print("Can donate blood")
        else:
            print("Unable to donate blood")
    else:
        print("Unable to donate blood due to your weight")    
else: # NOTE:Check on indentation.
    print("Unable to donate blood due to your age")

