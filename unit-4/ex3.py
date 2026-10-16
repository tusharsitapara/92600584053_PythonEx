''' 3. Write a program to illustrate instance variables and class variables. '''

class student:
    
    collage = "MU"
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        
obj = student('Tushar',1)
print(obj.name,obj.rollno,student.collage)

obj1 = student('Menil',2)
print(obj1.name,obj1.rollno,student.collage)


''' OUTPUT :
        Tushar 1 MU
        Menil 2 MU
'''