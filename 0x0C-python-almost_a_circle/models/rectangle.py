#!/usr/bin/python


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ returns x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns y attribute """
        return self.__y

    @y.setter
    def y(self, value):
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
        for i in range(0, self.height):
            print("#" * self.width)
