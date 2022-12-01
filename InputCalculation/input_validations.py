from MyConstantsAndExceptions.my_exceptions import *
from MyConstantsAndExceptions.constants import *


def is_operator(operator: str):
    if OPERATORS.count(operator) == 0:
        raise OperatorError(f"{operator} is not a legal operator in Omega calculator!")


def handle_parenthesis(arithmetic_expression: str):
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


