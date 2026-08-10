# 3. Write a program to perform arithmetic relational and logical operations using Python operators.

x = int(input("Enter Number 1 Here : "))
y = int(input("Enter Number 2 Here : "))

print("\n======= Arithmetic =======\n")
print("Addition is : ",x+y)
print("Substrection is : ",x-y)
print("Multipliction is : ",x*y)
print("Division is : ",x/y)
print("Modulo is : ",x%y)

print("\n======= Relational =======\n")
print("Equal Equal : ",x==y)
print("Not Equal : ",x!=y)
print("Graterthan : ",x>y)
print("Lessthan : ",x<y)
print("Graterthan Equal : ",x>=y)
print("Lessthan Equal : ",x<=y)

print("\n======= Logical =======\n")
m = bool(input("Enter (True/False) : "))
n = bool(input("Enter (True/False) : "))
print("AND Logical OP. : ",m and n)
print("OR Logical OP. : ",m or n)
print("NOT Logical OP. : ",not x == y)



