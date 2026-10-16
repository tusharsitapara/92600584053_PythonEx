''' 10. Write a program to perform file pointer 
operations using seek and tell methods. '''

f = open("demo.txt", "w+")
f.write("Hello Python")

print("Position:", f.tell())

f.seek(0)
print("Data:", f.read())

f.seek(6)
print("Position:", f.tell())
print("Data:", f.read())

f.close()


''' OUTPUT :
        Position: 12
        Data: Hello Python
        Position: 6
        Data: Python
'''