''' 10.Write a program to demonstrate recursion using 
factorial or Fibonacci series. '''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not possible for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
