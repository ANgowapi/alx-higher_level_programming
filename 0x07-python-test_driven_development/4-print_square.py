#!/usr/bin/python3
"""
This is the 4-print_square module.
The function print_square(size) prints a square with the # character.
"""

def print_square(size):
    """Prints a square with the # character.
    Args:
    - size(int): length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="")
                for j in range(size)]
        print("")