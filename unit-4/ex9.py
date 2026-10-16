''' 9. 9. Write a program to read and write data into a 
file using different file modes. '''

# Write data into a file
f = open("demo.txt", "w")
f.write("Hello Python")
f.close()

# Read data from a file
f = open("demo.txt", "r")
print(f.read())
f.close()

# Append data to a file
f = open("demo.txt", "a")
f.write("\nWelcome")
f.close()

# Read the updated file
f = open("demo.txt", "r")
print(f.read())
f.close()


''' OUTPUT :
        Hello Python
        Hello Python
        Welcome
'''