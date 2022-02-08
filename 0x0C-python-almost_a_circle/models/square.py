#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter to assign the width and height to the same value"""
        self.width = value
        self.height = value

    def __str__(self):
        """ method to returns [Rectangle] """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""
        args_list = ["id", "size", "x", "y"]
        if args and args[0] is not None:
            if len(args) > len(args_list):
                length = len(args_list)
            else:
                length = len(args)
            for tmp in range(length):
                setattr(self, args_list[tmp], args[tmp])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """dictionary"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y,
                }
