from ConstantsAndExceptions.constants import *


def reduce_minuses(arithmetic_expression: str) -> str:
    """
    the function reduces minuses in the received expression,
    for example: 2+---3*--4 --> 2+-3*4
    :param arithmetic_expression: the received expression
    :return: the expression with reduced minuses
    """
    before_minus = ''
    count_minus = 0
    new_expression = ""
    for i in range(len(arithmetic_expression)):
        if arithmetic_expression[i] == '-':
            count_minus += 1
        elif count_minus > 0:
            if count_minus % 2 == 0:
                if before_minus.isdigit() or before_minus in CLOSERS:
                    new_expression = new_expression.__add__('+' + arithmetic_expression[i])
                    before_minus = arithmetic_expression[i]
                else:
                    new_expression = new_expression.__add__(arithmetic_expression[i])
                    before_minus = arithmetic_expression[i]
                count_minus = 0
            else:
                new_expression = new_expression.__add__('-' + arithmetic_expression[i])
                before_minus = arithmetic_expression[i]
                count_minus = 0
        else:
            before_minus = arithmetic_expression[i]
            new_expression = new_expression.__add__(arithmetic_expression[i])
            count_minus = 0
    if count_minus > 0:
        new_expression = new_expression.__add__('-' * count_minus)
    return new_expression


def reduce_spaces(arithmetic_expression: str) -> str:
    """
    the function remove spaces from the received arithmetic expression
    :param arithmetic_expression: the received expression
    :return: the expression without spaces
    """
    for ignore_char in IGNORE:
        arithmetic_expression = arithmetic_expression.replace(ignore_char, '')
    return arithmetic_expression
