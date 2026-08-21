''' 7. Write a program to demonstrate list dictionary 
and set comprehensions. '''


print("--- List Comprehension ---")

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)


print("\n--- Dictionary Comprehension ---")

number_dict = {x: x * x for x in numbers}
print(number_dict)


print("\n--- Set Comprehension ---")

duplicate_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x * x for x in duplicate_numbers}
print(unique_squares)


''' OUTPUT :
            --- List Comprehension ---
            [1, 4, 9, 16, 25]

            --- Dictionary Comprehension ---
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

            --- Set Comprehension ---
            {1, 4, 9, 16, 25}
'''
