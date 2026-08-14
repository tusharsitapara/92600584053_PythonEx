''' 9. Write a program to define and use user-defined 
functions with different types of arguments. '''

print("Required arguments")

def add(a, b):
    sum = a + b
    return sum

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)

print("Sum =", result)

print("==================================================")
print("Default Argumant")

def default(name="Student"):
    print("Hello", name)

default()
default("Tushar")
