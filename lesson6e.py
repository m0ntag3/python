# On the  try and except block, you can run some codes/statements and if is is successful the try block will be executed other the except block will be executed when there is an anticipated error.

try:
    number = 100
    answer = number / 0
    print("The answer is:", answer)
except Exception as e:
    print("There is an error:", e)


try:
        numbers = [10,20,30]
        print("Your number is:", number[6])
except Exception as e:
        print("There is an error:", e)