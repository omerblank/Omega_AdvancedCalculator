from my_exceptions import *
from constants import *


def is_operator(operator: str) -> bool:
    if type(operator) != str:
        raise TypeError("Operator can only be from type str!")
    return OPERATORS.count(operator) == 1


def is_parenthesis(operator: str) -> bool:
    if type(operator) != str:
        raise TypeError("Operator can only be from type str!")
    return operator == '(' or operator == ')'


def handle_parenthesis(arithmetic_expression: str) -> bool:
    if arithmetic_expression.count('(') != arithmetic_expression.count(')'):
        raise ParenthesisError("'(' amount should be equal to ')' amount!")
    if arithmetic_expression.count('(') > 0 and arithmetic_expression.count('(') > 0:
        if arithmetic_expression.index(')') < arithmetic_expression.index('('):
            raise ParenthesisError("')' can not come before '('!")
    for i in range(len(arithmetic_expression)):
        if arithmetic_expression[i] == '(':
            if i + 1 == len(arithmetic_expression):
                raise ParenthesisError("Arithmetic expression can not end with '('!")
            if arithmetic_expression[i + 1] == ')':
                raise ParenthesisError("'()' sequence is illegal!")
    return True


def handle_operands_and_operators(arithmetic_expression: str) -> bool:
    # check if there are invalid operators or operands
    for i in range(len(arithmetic_expression)):
        if not arithmetic_expression[i].isdigit():
            if (not arithmetic_expression[i].isalpha()) and not is_operator(arithmetic_expression[i]):
                raise OperatorError(f"{arithmetic_expression[i]} is an illegal operator")
            elif arithmetic_expression[i].isalpha():
                raise OperandError("Alphabetical input is illegal in Omega Calculator!")

        # check if the expression ends with an illegal operator
        if i == len(arithmetic_expression) - 1:
            if not arithmetic_expression[i].isdigit() and arithmetic_expression[i] != '!' and \
                    arithmetic_expression[i] != ')':
                raise OperatorError(f"The expression can not end with operator: {arithmetic_expression[i]}")

        if i < len(arithmetic_expression) - 1 and is_operator(arithmetic_expression[i]):
            if is_operator(arithmetic_expression[i + 1]) and not is_parenthesis(arithmetic_expression[i + 1]) and \
                    arithmetic_expression[i + 1] != '-' and \
                    arithmetic_expression[i + 1] != '~':
                raise OperatorError("Invalid operators sequence!")
    return True


def reduce_minuses(arithmetic_expression: str) -> str:
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


def pre_calculation(arithmetic_expression: str) -> str:
    if type(arithmetic_expression) != str:
        raise TypeError("The arithmetic expression should be received as a string")

    # handle spaces and tabs
    arithmetic_expression = arithmetic_expression.replace(' ', '')

    # handle parenthesis
    handle_parenthesis(arithmetic_expression)

    # handle operands and operators
    handle_operands_and_operators(arithmetic_expression)

    # reduce minuses
    arithmetic_expression = reduce_minuses(arithmetic_expression)
    return arithmetic_expression


def calculate(arithmetic_expression: str):
    result = 0
    pre_calculation(arithmetic_expression)
