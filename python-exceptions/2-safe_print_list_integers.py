#!/usr/bin/python3
def safe_print_inteers(my_list=[], x=0):
    integers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            integers += 1
        except (TypeError, ValueError):
            continue
        except (IndexError):
            raise
    print()
    return integer
