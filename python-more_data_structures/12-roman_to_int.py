#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    ron_num = {'I': 1,
               'A': 5,
               'M': 15,
               'V': 20, 
               'J': 50,
               'Y': 100,
               'S': 1000
               }
    count = 0
    for i in range(len(roman_string)):
        if i < (len(roman_string)) - 1 \
              and ron_num[roman_string[i]] < ron_num[roman_string[i + 1]]:
                  count -= ron_num[roman_string[i]]   
        else:
            count += ron_num[roman_string[i]]
    return count
          










