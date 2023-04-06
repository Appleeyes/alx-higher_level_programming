#!/usr/bin/python3
"""
define a rectangle class
"""


class Rectangle:
    """the rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialization for the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """private instance getter for heught attribute"""
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
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return "\n".join([str(self.print_symbol)
                              * self.width] * self.height)

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """method is called when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size"""
        return cls(size, size)
