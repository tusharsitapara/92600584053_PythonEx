# 6. Write a program to illustrate the use of tuples and sets with basic operations.

print("======== TUPLES ========")
t1 = ("Ram","Mera","Radha","Kano")
t2 = (1,2,3,4,5)

print(len(t1))

print(t1+t2)

print(t2*3)

print(t1[0:])

print(t1[:2])

print(t1[-2])


print("\n======== SETS ========")
set_a = {"apple", "banana", "cherry", "apple"}
set_b = {"cherry", "dragonfruit", "elderberry"}

set_a.add("orange")
print("Set A after adding 'orange':", set_a)

set_a.remove("banana")
print("Set A after removing 'banana':", set_a)

print("Union (All items):", set_a.union(set_b))

print("Intersection (Common items):", set_a.intersection(set_b))

print("Difference (Set A - Set B):", set_a.difference(set_b))
