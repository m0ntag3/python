# Boolean
# A datatype that evaluates either true or false.

israining = False
print(israining)
print(type(israining))

# If the False/ True is in quotes it becomes a string.

paidloan = True
print(paidloan)
print(type(paidloan))

# Comparison opearators: USed to compare two or more statements and usually return a boolean answer.

number1 = 2
number2 = 5

# = - Assignment Operator

print("is number1 greater than number2?",number1 > number2)
print("is number1 less than number2?",number1 < number2)
print("is number1 greater than or equal to number2?",number1 >= number2)
print("is number1 less than or equal to number2?",number1 <= number2)
print("is number1 equal to number2?",number1 == number2)
print("is number1 not equal to number2?",number1 != number2)

# Logical Operators
# Logical AND - Returns true if and only if the conditions/statement evaluates to true.
print((3 > 1) and (7 > 6))

# Logical OR - Evaluates to true if one of the statements/condition is true.
print((3 > 1) or (7 < 6))
print((3 < 1) or (7 < 6))

# Logical NOT - Negates a statement/condition.
print(not(90 > 70))
