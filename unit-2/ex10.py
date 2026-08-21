''' 10.Write a program to generate a sequence of 
numbers using generator functions and yield 
keyword. '''

def gen(limit):
    count = 1
    while count <= limit:
        yield count 
        count += 1

numbers = gen(3)

print("Sequence:")
for num in numbers:
    print(num)


''' OUTPUT :
            Sequence:
            1
            2
            3
'''
