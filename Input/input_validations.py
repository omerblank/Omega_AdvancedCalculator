# module for validations on the input
from Brackets.brackets_classes import *
from Operators.operators_classes import *


def validate_operator_in_expression(arithmetic_expression: str, index: int) -> None:
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
        if (OPERATORS_AND_CLASSES.get(operator).__base__ == TwoOperands) or operator in RIGHT_UNARY:
            raise OperatorError(f"{operator} can't open an expression!")
        OPERATORS_AND_CLASSES.get(operator)(None, arithmetic_expression[index + 1])
    elif index == len(arithmetic_expression) - 1:
        if OPERATORS_AND_CLASSES.get(operator).__base__ == TwoOperands or operator in LEFT_UNARY:
            raise OperatorError(f"{operator} can't close an expression!")
        OPERATORS_AND_CLASSES.get(operator)(arithmetic_expression[index - 1], None)
    else:
        OPERATORS_AND_CLASSES.get(operator)(arithmetic_expression[index - 1], arithmetic_expression[index + 1])


def validate_bracket_in_expression(arithmetic_expression: str, index: int) -> None:
    """
    the function validates bracket in the received expression
    :param arithmetic_expression: the received expression
    :param index: the index of the operator
    :return: None if the bracket is valid, Exception if not
    """
    bracket = arithmetic_expression[index]
    if arithmetic_expression.count('(') != arithmetic_expression.count(')'):
        raise BracketsError("'(' and ')' amount should be equal!")
    if arithmetic_expression[:index + 1].count('(') < arithmetic_expression[:index + 1].count(')'):
        raise BracketsError("missing '('")
    if index == 0:
        if bracket == ')':
            raise BracketsError(f"{bracket} can't open an expression!")
        BRACKETS_AND_CLASSES.get(bracket)(None, arithmetic_expression[index + 1])
    elif index == len(arithmetic_expression) - 1:
        if bracket == '(':
            raise BracketsError(f"{bracket} can't close an expression!")
        BRACKETS_AND_CLASSES.get(bracket)(arithmetic_expression[index - 1], None)
    else:
        BRACKETS_AND_CLASSES.get(bracket)(arithmetic_expression[index - 1], arithmetic_expression[index + 1])


# todo: fix this function!
def is_signed(arithmetic_expression: str, index: int) -> bool:
    """
    this function checks if a minus is a sign or an operator
    :param arithmetic_expression: the arithmetic expression
    :param index: the index of current minus in the expression
    :return: True if a minus is a sign and False if it is operator
    """
    minus = arithmetic_expression[index]
    if index == 0 and \
            (arithmetic_expression[index + 1] in OPENERS or arithmetic_expression[index + 1] in LEFT_UNARY
             or validate_right(arithmetic_expression[index + 1], minus)):
        return True
    elif index < len(arithmetic_expression) - 1 and \
            (arithmetic_expression[index - 1] in TWO_OPERANDS or arithmetic_expression[index - 1] in OPENERS or
             arithmetic_expression[index - 1] in LEFT_UNARY) and \
            (arithmetic_expression[index + 1] in OPENERS or arithmetic_expression[index + 1] in LEFT_UNARY
             or validate_right(arithmetic_expression[index + 1], minus)):
        return True
    return False


# todo make this function shorter!
def signed_operand(arithmetic_expression: str) -> str:
    """
    this function makes signed minuses in the expression calculable
    :param arithmetic_expression: the arithmetic expression
    :return: the expression after making its signed minuses calculable
    """
    new_expression = ""
    index = 0
    signed_flag, bracket_flag = False, False
    while index < len(arithmetic_expression):
        if arithmetic_expression[index] == '-':
            if is_signed(arithmetic_expression, index):
                signed_flag = True
                if index < len(arithmetic_expression) - 1 and arithmetic_expression[index + 1] in LEFT_UNARY:
                    # new_expression = new_expression.__add__("~(")
                    index += 2
                    signed_flag = False
                    continue
                else:
                    new_expression = new_expression.__add__("(~")
                index += 1
                continue
        if index < len(arithmetic_expression) - 1 and arithmetic_expression[index] in LEFT_UNARY and \
                arithmetic_expression[index + 1] == '-':
            index += 2
            signed_flag = False
            continue
        if arithmetic_expression[index] == '(':
            bracket_flag = True
        if arithmetic_expression[index] == ')':
            bracket_flag = False
        if signed_flag and not bracket_flag and \
                (arithmetic_expression[index] in TWO_OPERANDS or
                 arithmetic_expression[index] in OPENERS):
            new_expression = new_expression.__add__(")")
            signed_flag = False
        new_expression = new_expression.__add__(arithmetic_expression[index])
        index += 1
    while new_expression.count('(') != new_expression.count(')'):
        new_expression = new_expression.__add__(")")
    return new_expression
