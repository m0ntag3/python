#  Functions with paramaters
# Parameters - Values that get passed as arguments given/written in a function inside the parenthesis.

def greeting(name):
    print(f"{name},how are you? Hope everything is fine.")

greeting("Collins")
greeting("Poly")
greeting("Lilian")

print("=======================")
def message(names):
    print(f"Hello {names}, we shall be having a general meeting on date... Please avail yourself.")

message("Yosef")
message("Reigners")

print("===================")
def sum(x,y):
    addition = x + y
    print(f"The sum of the numbers is",addition)

sum(10,12)
sum(89,9)
