#!/usr/bin/python
""" module that contains Rectangle class """
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init the rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """setter width method"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def height(self):
        """ returns height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """setter height method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ returns x coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """setter width method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """setter width method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    """
    Task 4.
    """
    def area(self):
        """ returns area value of the rectangle """
        return self.width * self.height

    """
    Task 5.
    """
    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    """
    Task 6.
    """
    def __str__(self):
        """returns..."""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
                format(self.id, self.__x, self.__y, self.__width, self.__height)

    """
    Task 8.
    """
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:

1st argument should be the id attribute
2nd argument should be the width attribute
3rd argument should be the height attribute
4th argument should be the x attribute
5th argument should be the y attribute"""
        args_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                max_len = len(args_list)
            else:
                max_len = len(args)
            for i in range(max_len):
                setattr(self, args_list[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """dictionary"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }
