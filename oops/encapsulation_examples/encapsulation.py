class Car:
    def __init__(self, make='Ford', model='Pinto', year='1971', color='orange'):
        self._make = make
        self.__model = model
        self.__year = year
        self.__color = color

    def move_forward(self, speed):
        print("Your %s is moving forward at %s" % (self.__model, speed))

    def move_backward(self, speed):
        print("Moving backward at %s" % speed)


mycar = Car()

print mycar._Car__model # This is how you access __ attribute
# print mycar.__model
