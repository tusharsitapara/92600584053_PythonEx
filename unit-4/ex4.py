''' 4. Write a program to demonstrate instance methods class methods and static methods. '''

class A:
    value = 10

    def instance_method(self):
        print("Instance method called")

    @classmethod
    def class_method(cls):
        print("Class method called, class value is",cls.value)

    @staticmethod
    def static_method():
        print("Static method called")

obj = A()

obj.instance_method()
A.class_method()
A.static_method()


''' OUTPUT :
        Instance method called
        Class method called, class value is 10
        Static method called
'''