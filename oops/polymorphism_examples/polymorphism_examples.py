class ParentClass:
    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from ParentClass")


class ChildClass(ParentClass):
    def __init__(self):
        self.__y = 1
 
    def m1(self):
        print("m1 from ChildClass")


c = ChildClass()
c.m1()
