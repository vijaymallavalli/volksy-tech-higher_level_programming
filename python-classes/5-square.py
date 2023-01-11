#!/usr/bin/python3
"""printing the squares"""

class Square:
    """privitate instance of the class"""
    def size(self, value):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not integer:
            raise TypeError("size must be an integer")
      if type(size) < 0:
          raise ValueError("size must be >= 0")
      self.__size = size

    def area(size):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
