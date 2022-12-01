from ConstantsAndExceptions.exceptions import *
from ConstantsAndExceptions.constants import *


# def handle_parenthesis(arithmetic_expression: str):
#     if arithmetic_expression.count('(') != arithmetic_expression.count(')'):
#         raise BracketsError("'(' amount should be equal to ')' amount!")
#     if arithmetic_expression.count('(') > 0 and arithmetic_expression.count('(') > 0:
#         if arithmetic_expression.index(')') < arithmetic_expression.index('('):
#             raise BracketsError("')' can not come before '('!")
#     for i in range(len(arithmetic_expression)):
#         if arithmetic_expression[i] == '(':
#             if i + 1 == len(arithmetic_expression):
#                 raise BracketsError("Arithmetic expression can not end with '('!")
#             if arithmetic_expression[i + 1] == ')':
#                 raise BracketsError("'()' sequence is illegal!")


# def handle_operands_and_operators(arithmetic_expression: str) -> bool:
#     # check if there are invalid operators or operands
#     for i in range(len(arithmetic_expression)):
#         if not arithmetic_expression[i].isdigit():
#             if (not arithmetic_expression[i].isalpha()) and not is_operator(arithmetic_expression[i]):
#                 raise OperatorError(f"{arithmetic_expression[i]} is an illegal operator")
#             elif arithmetic_expression[i].isalpha():
#                 raise OperandError("Alphabetical input is illegal in Omega Calculator!")
#
#         # check if the expression ends with an illegal operator
#         if i == len(arithmetic_expression) - 1:
#             if not arithmetic_expression[i].isdigit() and arithmetic_expression[i] != '!' and \
#                     arithmetic_expression[i] != ')':
#                 raise OperatorError(f"The expression can not end with operator: {arithmetic_expression[i]}")
#
#         if i < len(arithmetic_expression) - 1 and is_operator(arithmetic_expression[i]):
#             if is_operator(arithmetic_expression[i + 1]) and not is_parenthesis(arithmetic_expression[i + 1]) and \
#                     arithmetic_expression[i + 1] != '-' and \
#                     arithmetic_expression[i + 1] != '~':
#                 raise OperatorError("Invalid operators sequence!")
#     return True


def reduce_minuses(arithmetic_expression: str) -> str:
    """
    the function reduces minuses in the received expression,
    for example: 2+---3*--4 --> 2+-3*4
    :param arithmetic_expression: the received expression
    :return: the expression with reduced minuses
    """
    count_minus = 0
    new_expression = ""
    for i in range(len(arithmetic_expression)):
        if arithmetic_expression[i] == '-':
            count_minus += 1
        elif arithmetic_expression[i].isdigit() and count_minus > 0:
            if count_minus % 2 == 0:
                new_expression = new_expression.__add__(arithmetic_expression[i])
            else:
                new_expression = new_expression.__add__('-' + arithmetic_expression[i])
        else:
            new_expression = new_expression.__add__(arithmetic_expression[i])
            count_minus = 0
    return new_expression


def validate_and_reduce_spaces(arithmetic_expression: str) -> str:
    """
    the function validates spaces locations and reduces them if their locations are valid
    :param arithmetic_expression: the received expression
    :return: Exception if spaces are not valid, if they are, returns the expression without spaces
             invalid spaces example: 3 4+5
             valid spaces example: 34 + 5
    """
    pass


def validate_operator_in_expression(arithmetic_expression: str, index: int):
    """
    the function validates operator in the received expression
    :param arithmetic_expression: the received expression
    :param index: the index of the operator
    :return: None if the operator is valid, Exception if not
    """
    operator = arithmetic_expression[index]
    if operator not in OPERATORS:
        raise OperatorError(f"{operator} is unidentified!")
    if index == 0:
        if (OPERATORS.get(operator).__base__ == TwoOperands and operator != '-') or ONE_OPERAND.get(
                operator) == "right":
            raise OperatorError(f"{operator} can't open an expression!")
        OPERATORS.get(operator)(None, arithmetic_expression[index + 1])
    elif index == len(arithmetic_expression) - 1:
        if OPERATORS.get(operator).__base__ == TwoOperands or ONE_OPERAND.get(
                operator) == "left":
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
