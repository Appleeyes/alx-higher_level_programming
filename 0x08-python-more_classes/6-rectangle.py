#!/usr/bin/python3
"""
define a rectangle class
"""


class Rectangle:
     """the rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialization for the class"""
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """private instance getter for width attribute"""
        return self._width
    
    @width.setter
    def width(self, value):
        """private instance setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
    
    @property
    def height(self):
        """private instance getter for heught attribute"""
        return self._height
    
    @height.setter
    def height(self, value):
        """private instance setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
    
    def area(self):
        """returns the rectangle area"""
        return self._width * self._height
    
    def perimeter(self):
        """returns the rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
    
    def __str__(self):
        """returns a string representation of the rectangle using the #"""
        if self._width == 0 or self._height == 0:
            return ''
        return '\n'.join(['#' * self._width] * self._height)
    
    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f'Rectangle({self._width}, {self._height})'
    
    def __del__(self):
        """method is called when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
