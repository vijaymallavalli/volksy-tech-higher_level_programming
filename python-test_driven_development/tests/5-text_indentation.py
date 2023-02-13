#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """indentation"""

    if type(text) != str or text is None or len(text) < 0:
        raise TypeError("text mustbe a string")
    aux = 0
    for c in text:
        if c == '?' or c ==':' or c =='.':
            print(c, end="\n\n")
            aux = 1
        else:
            if aux == 0:
                print(c,end="")
            else:
                if c == ' ' or c == '\t':
                    pass
                else:
                    print(c, end="")
                    aux = 0
