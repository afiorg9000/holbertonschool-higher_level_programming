#!/usr/bin/python3
"""Defines classes for singly linked lists"""


class Node:
    """Represents a node"""
    def __init__(self, data, next_node=None):
        """initialized a node"""
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Represent a singly-linked list."""

    def init(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None:
            new.next_node = None
            self.head = new
        elif self.head.data > value:
            new.next_node = self.__head
            self.head = new
        else:
            tmp = self.head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def str(self):
        values = []
        tmp = self.head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
