#!/usr/bin/python3
"""coordinates of a squares"""


class Squares:
    """squares"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @set.setter
    def size(self,size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        sel.__size = size

    @property
    def position(self):
        return self.__position

    @set.setter
    if self.__size is 0:
        print("")
        return
    for i in range(self.__position[1]):
        print("")
    for i in range(self.__size):
        print(" " * self.__position[0], end="")
        print("#" * self.__size)
