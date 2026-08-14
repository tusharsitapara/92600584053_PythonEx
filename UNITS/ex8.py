''' 8. Write a program to explain mutable and 
immutable objects in Python. '''




print("Immutable object")
a = 10
print("Before:", a)

a = 20
print("After:", a)

print("Mutable object")
numbers = [10, 20, 30]
print("Before:", numbers)

numbers.append(40)
print("After:", numbers)
