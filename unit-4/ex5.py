''' 5. Write a program to implement single multilevel and multiple inheritance. '''

class Parent:
    def feature1(self):
        print("Feature 1 from Parent")

class Child(Parent):
    def feature2(self):
        print("Feature 2 from Child")


class GrandChild(Child):
    def feature3(self):
        print("Feature 3 from GrandChild")


class Friend:
    def feature4(self):
        print("Feature 4 from Friend")

class MultiChild(Parent, Friend):
    def feature5(self):
        print("Feature 5 from MultiChild")


print("=== Single Inheritance ===")
obj1 = Child()
obj1.feature1()
obj1.feature2()

print("\n=== Multilevel Inheritance ===")
obj2 = GrandChild()
obj2.feature1()
obj2.feature2()
obj2.feature3()

print("\n=== Multiple Inheritance ===")
obj3 = MultiChild()
obj3.feature1()
obj3.feature4()
obj3.feature5()


''' OUTPUT :
        === Single Inheritance ===    
        Feature 1 from Parent
        Feature 2 from Child

        === Multilevel Inheritance ===
        Feature 1 from Parent
        Feature 2 from Child
        Feature 3 from GrandChild

        === Multiple Inheritance ===
        Feature 1 from Parent
        Feature 4 from Friend
        Feature 5 from MultiChild
'''