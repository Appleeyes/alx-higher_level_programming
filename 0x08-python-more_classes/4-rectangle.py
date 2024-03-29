#!/usr/bin/python3
"""
define a rectangle class
"""


class Rectangle:
    """the rectangle class"""
    def __init__(self, width=0, height=0):
        """initialization for the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string representation of the rectangle using the #"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            if i is not self.__height - 1:
                str += "\n"
        return str

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'
