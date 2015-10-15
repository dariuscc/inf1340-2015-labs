#!/usr/bin/env python3

""" Graded Lab #2 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


"""
Instructions: Add a function to to get input from the user and use that
function in name_that_shape()

The function should prompt the user for input until a legal value is
entered. A legal value is any integer.

"""

def get_legal_input():
    legal_input = 0
    valid_input = False
    while(valid_input == False):
        #Using substring comparison
        user_input = raw_input("Number of sides:")
        # decimals with .isdigit() returns False (i.e. "2.5".isdigit() == False)
        if(user_input.isdigit()):
            valid_input = True
            legal_input = user_input
        # minus sign with .isdigit() returns False (i.e. "-3".isdigit() == False)
        # but that is valid input. So the initial minus sign is checked and the rest is checked with .isdigit()
        if(user_input[0] == "-" and user_input[1:].isdigit()):
            valid_input = True
            legal_input = user_input
    return int(legal_input)

def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs | Expected Outputs
    -------------------------
      < 3  | Error
      3    | triangle
      4    | quadrilateral
      5    | pentagon
      6    | hexagon
      7    | heptagon
      8    | octagon
      9    | nonagon
      10   | decagon
      > 10 | Error

    Errors: ValueError when input is a string or float

    """

    sides = get_legal_input()

    if sides == 3:
        print("triangle")
    elif sides == 4:
        print("quadrilateral")
    elif sides == 5:
        print("pentagon")
    elif sides == 6:
        print("hexagon")
    elif sides == 7:
        print("heptagon")
    elif sides == 8:
        print("octagon")
    elif sides == 9:
        print("nonagon")
    elif sides == 10:
        print("decagon")
    else:
        print("Error")

# name_that_shape()
