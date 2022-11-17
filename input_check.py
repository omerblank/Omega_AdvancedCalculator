from my_exceptions import *


def input_check(arithmetic_expression: str):
    if type(arithmetic_expression) != str:
        raise TypeError("The arithmetic expression should be received as a string")

    # handle spaces and tabs
    arithmetic_expression = arithmetic_expression.replace(' ', '')

    # handle parenthesis
    if arithmetic_expression.count('(') != arithmetic_expression.count(')'):
        raise ParenthesisError("'(' amount should be equal to ')' amount!")
    #todo: handle the case we have () at the beggining of an expression - ()4+3()
