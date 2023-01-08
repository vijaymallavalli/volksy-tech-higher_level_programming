#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
         [print("{}: {}".format(v, a_dictionary[v])) for v in sorted(a_dictionary)]
