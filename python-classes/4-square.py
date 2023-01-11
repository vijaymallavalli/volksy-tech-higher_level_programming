#!/usr/bin/python3
"""size of square"""


class Square:
    """size of square"""
    def __init__(self, size=0):
        """size of square"""
        self.__size = size


     @property
     def size(self):
         """size of  square"""
         return self.__size = size

     @size.setter
     def size(self, value):
         """self swiw of the square"""
         if type(size) is not a integer:
             raise TypeError("size must be an integer")
         if size < 0:
             raise ValueError("size must be >= 0")
         self.__size = size

     def area(self):
         return(self.__size * slf.__size)

