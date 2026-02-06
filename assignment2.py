# Tuple of 8 planets
planets = ("Mercury","Venus", "Earth", "Mars","Jupiter", "Saturn", "Uranus", "Neptune")
print(planets)
print(planets [2:7] )

print("==============")

# IF.......ELSE statements
# Basic Syntax
age = 18

if age >= 18:
    print("ID eligible")
else:
    print("Too young for ID")


age = 16

if age >= 18:
    print("ID eligible")
else:
    print("Too young for ID")    

print("==============")    
# Handling Multiple Conditions
# if: The first check.
#elif: Checked only if the previous conditions were False.
#else: The "catch-all" if nothing else matched.

marks = 84

if marks >= 80:
    print("A Grade")
elif marks >= 75:
    print("A- Grade")    
elif marks >= 70:
    print("B+ Grade")
else:
    print("C+ Grade")

marks = 73

if marks >= 80:
    print("A Grade")
elif marks >= 75:
    print("A- Grade")    
elif marks >= 70:
    print("B+ Grade")
else:
    print("C+ Grade") 

marks = 56

if marks >= 80:
    print("A Grade")
elif marks >= 75:
    print("A- Grade")    
elif marks >= 70:
    print("B+ Grade")
else:
    print("C+ Grade") 

print("==============")
# One-Liner (ternary operator)
# Basically fits several code lines in one therefore simplifying the code.

score = 60
stature = "Good" if score >= 70 else "Try harder"
print(stature)

score = 78
stature = "Good" if score >= 70 else "Try harder"
print(stature)

print("==============")
# Logical operators
# Involves the use of:
# and: True if both are true.
# or: True if at least one is true.
# not: Flips the result (True becomes False).

has_grade = True
is_displine = True

if has_grade and is_displine:
    print("Eligible to study")
else:
    print("Invalid school entry")

has_grade = True
is_indispline = False

if has_grade or is_displine:
    print("Eligible to study")
else:
    print("Invalid school entry")

hasnot_grade = False
is_indispline = False

if has_grade and is_displine:
    print("Eligible to study")
else:
    print("Invalid school entry")

# Nested IF
weight = 60
height = 1.55

if weight < 50:
    if height > 1.95:
        print("Able to participate in the basketball game")
    else:
        print("Unable to participate in the basketball game")    
else:
    print("Unable to participate in the basketball game")      