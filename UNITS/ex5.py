# 5. Write a program to create and manipulate lists using indexing slicing and list comprehensions.

list1 = ["Apple","Banana","Cherry","Watermelon","Orange"]

print(list1[1:2])

list1.insert(1,"Grappes")
print(list1)

print(list1[2])
print(list1[:2])
print(list1[-2])
print(list1[::2])
print(list1[0:])


l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l1.extend(l2)
print(l1)
l1.remove(1)
print(l1)


"""
    OUTPUT :

    ['Banana']
    ['Apple', 'Grappes', 'Banana', 'Cherry', 'Watermelon', 'Orange']
    Banana
    ['Apple', 'Grappes']
    Watermelon
    ['Apple', 'Banana', 'Watermelon']
    ['Apple', 'Grappes', 'Banana', 'Cherry', 'Watermelon', 'Orange']
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
