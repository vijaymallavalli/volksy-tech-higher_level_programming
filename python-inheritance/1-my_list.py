#!/usr/bin/python3
"""My list """

class Mylist(list):
    """hat prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """sorted list """
        print(sorted(self))
