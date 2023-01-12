#!/usr/bin/python3
"""size of square"""


class Square:
    """represents a sqauare"""
    def __init__(self, size=0, poition=(0, 0)):
        """"initiallizes the data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the square"""
        return self.__size**2

    def my_print(self):
        """print the sqiare"""
        if self.__size == 0:
            print()
        else:
            prinnt('\n' * self.__position[1\], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)



