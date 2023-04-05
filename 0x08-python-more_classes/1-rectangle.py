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
