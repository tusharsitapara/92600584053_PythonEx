''' 1. Write a program to create a class and object in Python. '''

class A:
    num = 100
    
    def hello(self):
        print("Hello Function!")

obj = A()

print(obj.num)

obj.hello()


'''OUTPUT :
        100
        Hello Function!
'''