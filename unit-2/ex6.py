''' 6. Write a program to iterate over lists strings and 
dictionaries using loops. '''


print("\n===List=== \n")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n===String=== \n")
word = "Python"
for letter in word:
    print(letter)

print("\n===Dictionary=== \n")
scores = {"Kano": 90, "Tushar": 85, "Menil": 95}

for name, score in scores.items():
    print(name, "scored", score)


""" OUTPUT:

        ===List=== 

        apple
        banana
        cherry

        ===String=== 

        P
        y
        t
        h
        o
        n

        ===Dictionary=== 

        Kano scored 90
        Tushar scored 85
        Menil scored 95
""""
