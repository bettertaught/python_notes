class Rectangle:
    def __int__(self, color, filled, width, length):
        self.__color = color
        self.__filled = filled
        self.__width = width
        self.__length = length
 
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        return self.__color = color
 
    def is_filled(self):
        return self.__filled
 
    def set_filled(self, filled):
        return self.__filled
 
    def get_area():
        return self.__width * self.__length

