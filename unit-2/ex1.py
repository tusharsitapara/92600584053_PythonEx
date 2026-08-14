''' 1. Write a program to demonstrate conditional 
statements using if if-else and if-elif-else. '''



num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")

print("==========================================")
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("==========================================")
if num > 0:
    print("Number is greater than zero")
elif num < 0:
    print("Number is less than zero")
else:
    print("Number is zero")
