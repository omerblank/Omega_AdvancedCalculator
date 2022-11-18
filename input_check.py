from my_exceptions import *


def input_check(arithmetic_expression: str):
    operators = ['+', '-', '*', '/', '%', '^', '$', '&', '@', '~', '!', '(', ')']
    if type(arithmetic_expression) != str:
        raise TypeError("The arithmetic expression should be received as a string")

    # handle spaces and tabs
    arithmetic_expression = arithmetic_expression.replace(' ', '')

    # handle parenthesis
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

    # handle operands and operators
    for char in arithmetic_expression:
        if not char.isdigit():
            if (not char.isalpha()) and operators.count(char) == 0:
                raise OperatorError(f"{char} is an illegal operator")
            elif char.isalpha():
                raise OperandError("Alphabetical input is illegal in Omega Calculator!")
