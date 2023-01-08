#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    count = 0
    for i in my_list:
        count += i
    return count
