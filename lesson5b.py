#functions with parameters
# Paremeters: they are values that get passed as arguments given to a function inside of the parenthesis.

def greetings(name):
    print(f"{name},How are you? Hope everything is fine.")
greetings("Victoria")

print("====================")

def message (names):
    print(f"Hello {names} we shall be having a general meeting on date... please avail yporself.")
message("Abel")
message("Eve")

print("====================")
#create function that accepts parameters to add two numbers
def addition(a ,b):
    sum = a + b
    print("the sum of the numbers is:", sum)
addition(35,57)
addition(52,86)