''' 8. Write a program to illustrate variable scope 
using local global and nonlocal variables. '''


x = "Global"

def outer():
    x = "Nonlocal"
    
    def inner():
        x = "Local"
        print("1. Inner Function:", x)
        
    def change():
        nonlocal x
        x = "Changed Nonlocal"
        
    inner()
    change()
    print("2. Outer Function:", x)

outer()
print("3. Outside Everything:", x)


''' OUTPUT :
        1. Inner Function: Local
        2. Outer Function: Changed Nonlocal
        3. Outside Everything: Global
'''
