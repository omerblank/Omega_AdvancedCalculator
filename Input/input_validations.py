from Brackets.brackets_classes import *
from Operators.operators_classes import *


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
    the function validates spaces locations and reduces them
    :param arithmetic_expression: the received expression
    :return: the expression without spaces
    """
    return arithmetic_expression.replace(' ', '')


def validate_operator_in_expression(arithmetic_expression: str, index: int):
    """
    the function validates operator in the received expression
    :param arithmetic_expression: the received expression
    :param index: the index of the operator
    :return: None if the operator is valid, Exception if not
    """
    operator = arithmetic_expression[index]
    if operator not in OPERATORS:
        raise ValueError(f"{operator} is unidentified!")
    elif index == 0:
        if (OPERATORS.get(operator).__base__ == TwoOperands) or operator in RIGHT_UNARY:
            raise OperatorError(f"{operator} can't open an expression!")
        OPERATORS.get(operator)(None, arithmetic_expression[index + 1])
    elif index == len(arithmetic_expression) - 1:
        if OPERATORS.get(operator).__base__ == TwoOperands or operator in LEFT_UNARY:
            raise OperatorError(f"{operator} can't close an expression!")
        OPERATORS.get(operator)(arithmetic_expression[index - 1], None)
    else:
        OPERATORS.get(operator)(arithmetic_expression[index - 1], arithmetic_expression[index + 1])


def validate_bracket_in_expression(arithmetic_expression: str, index: int):
    """
    the function validates bracket in the received expression
    :param arithmetic_expression: the received expression
    :param index: the index of the operator
    :return: None if the bracket is valid, Exception if not
    """
    bracket = arithmetic_expression[index]
    if arithmetic_expression.count('(') != arithmetic_expression.count(')'):
        raise BracketsError("'(' and ')' amount should be equal!")
    if arithmetic_expression[:index+1].count('(') < arithmetic_expression[:index+1].count(')'):
        raise BracketsError("missing '('")
    if index == 0:
        if bracket == ')':
            raise BracketsError(f"{bracket} can't open an expression!")
        BRACKETS.get(bracket)(None, arithmetic_expression[index + 1])
    elif index == len(arithmetic_expression) - 1:
        if bracket == '(':
            raise BracketsError(f"{bracket} can't close an expression!")
        BRACKETS.get(bracket)(arithmetic_expression[index - 1], None)
    else:
        BRACKETS.get(bracket)(arithmetic_expression[index - 1], arithmetic_expression[index + 1])


# todo: fix this function!
def is_signed(arithmetic_expression: str, index: int):
    minus = arithmetic_expression[index]
    if index == 0 and (
            arithmetic_expression[index + 1] in OPENERS or validate_right(arithmetic_expression[index + 1], minus)):
        return True
    if (arithmetic_expression[index - 1] in TWO_OPERANDS or arithmetic_expression[index - 1] in OPENERS or
        arithmetic_expression[index - 1] in LEFT_UNARY) and (
            arithmetic_expression[index + 1] in OPENERS or validate_right(arithmetic_expression[index + 1], minus)):
        return True
    return False


def signed_operand(arithmetic_expression: str):
    new_expression = ""
    index = 0
    while index < len(arithmetic_expression):
        if arithmetic_expression[index] == '-':
            if is_signed(arithmetic_expression, index):
                new_expression = new_expression.__add__('~')
                index += 1
                continue
        new_expression = new_expression.__add__(arithmetic_expression[index])
        index += 1
    return new_expression
