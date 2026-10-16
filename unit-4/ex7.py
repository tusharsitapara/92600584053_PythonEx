''' 7. Write a program to illustrate method resolution order and magic methods. '''

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def __str__(self):
        return "Class C"

obj = C()

obj.show()
print(obj)
print(C.mro())


''' OUTPUT :
        Class B
        Class C
        [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
'''