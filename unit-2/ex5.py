''' 5. Write a program to demonstrate the use of 
break continue and pass statements.  '''

print("--- Break ---")
for x in range(1, 5):
    if x == 3:
        break
    print(x)


print("\n--- Continue ---")
for x in range(1, 5):
    if x == 3:
        continue
    print(x)


print("\n--- Pass ---")
for x in range(1, 5):
    if x == 3:
        pass
    print(x)
    

""" OUTPUT :

        --- Break ---
        1
        2

        --- Continue ---
        1
        2
        4

        --- Pass ---
        1
        2
        3
        4
"""
