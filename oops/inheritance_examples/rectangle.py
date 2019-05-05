class Rectangle:
    def __init__(self, color, filled, width, length):
        self.__color = color
        self.__filled = filled
        self.__width = width
        self.__length = length
 
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
        return self.__width * self.__length
