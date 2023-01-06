#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        lst=[]
        if i != 'c' and i != 'C':
            lst.append(i)
    return "".join(lst)
