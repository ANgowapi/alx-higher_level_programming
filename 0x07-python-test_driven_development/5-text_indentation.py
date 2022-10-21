#!/usr/bin/python3
"""
This is the 5-text_indentation module.
The function text_indentation(text) prints a text with 2 new lines after '.', '?' and ':'
"""

def text_indentation(text):
    """Prints text with 2 new lines after '.', '?' and ':'
    Args:
    - text(str): the text to print.
    Raises:
    - TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
