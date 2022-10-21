#!/usr/bin/python3
"""
This is the 3-say_my_name module.
The function say_my_name(first_name, last_name="") prints the first and last name.
"""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.
    Args:
    - first_name (str): First string to print
    - last_name (str): second string to print

    Raises:
    - TypeError: Exception if arguments aren't string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
