''' 2. Write a program to check whether a number is 
positive negative or zero using nested conditions. '''


num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")
