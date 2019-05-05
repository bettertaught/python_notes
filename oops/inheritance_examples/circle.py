import math


class Circle:
    def __init__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius      
 
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
        return self.__color

    def is_filled(self):
        return self.__filled
 
    def set_filled(self, filled):
        return self.__filled
 
    def get_area(self):
        return math.pi * self.__radius ** 2
