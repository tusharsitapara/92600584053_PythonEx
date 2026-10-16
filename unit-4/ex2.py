''' 2. Write a program to demonstrate constructor and destructor usage. '''

class A:
    
    def __init__(self,add,sub): #constructor
        self.add = add
        self.sub = sub
        
    def disp(self):
        print("Adition     :" ,self.add)
        print("Subtraction :" ,self.sub)
        
    def __del__(self): #destructor
        print("Destructor: Object destroyed.")
                
obj = A(10 + 20, 20 - 10)

obj.disp()

del obj


''' OUTPUT :

        Adition     : 30
        Subtraction : 10
        Destructor: Object destroyed.

'''