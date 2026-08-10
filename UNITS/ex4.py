# 4. Write a program to demonstrate string operations including slicing formatting and built-in string functions.

x = input("Enter String Here : ")

print(x[0:3])

print(x.upper())

print(x.lower())

print(x.capitalize())

print(x.title())

print(x.strip())

print(x.replace(x,"Sitapara"))

print("Python".find("o"))

print("This is Python".count("i"))

print(x.split(" "))

print("-".join(x))

print("Python".startswith("Py"))

print("Python".endswith("on"))

print(x.isalpha())

print(x.isdigit())

print(len(x))

"""
    OUTPUT :
    
    Enter String Here : tushar sitapara
    tus
    TUSHAR SITAPARA
    tushar sitapara
    Tushar sitapara
    Tushar Sitapara
    tushar sitapara
    Sitapara
    4
    2
    ['tushar', 'sitapara']
    t-u-s-h-a-r- -s-i-t-a-p-a-r-a
    True
    True
    False
    False
    15
"""
