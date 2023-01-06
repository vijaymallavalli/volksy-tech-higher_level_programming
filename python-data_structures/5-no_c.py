#!/usr/bin/python3
def no_c(my_string):
    lst = []
    for i in my_string:
        if i != 'c' and i != 'C':
            lst.append(i)
    return "".join(lst)
