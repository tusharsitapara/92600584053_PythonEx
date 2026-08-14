''' 7. Write a program to create a dictionary and 
demonstrate dictionary methods and iteration. '''

a_dict = {'Name': 'Ashu', 'Age': 7, 'Class': 'First'}

print(type(a_dict))
print(a_dict)

print ("Length ",len(a_dict))

a_dict.update({"city": "Mumbai"})
print("Updated Dict",a_dict)

del a_dict["city"]
print("Delect city",a_dict)

b_dict = a_dict.copy()
print("New Dictionary :",b_dict)



