from MyConstantsAndExceptions.constants import *


def digits_to_number(arithmetic_expression: str, index: int):
    """
    the function gets an expression and returns a number from the given index in the expression
    until the expression is over or the number is over
    and returns the new index after scanning the whole number in the expression
    :param arithmetic_expression: the arithmetic expression
    :param index: the index of an initial char which is a digit
    :return: the total number and the new index
    """
    number = arithmetic_expression[index]
    # loop until the number is over or until the expression is over
    while index + 1 != len(arithmetic_expression) and (arithmetic_expression[index + 1].isdigit() or
                                                       arithmetic_expression[index + 1] == '.'):
        number += arithmetic_expression[index + 1]
        index += 1
    if number.isdigit():
        return int(number), index
    return float(number), index


def operate_and_push(operators_stack: list, operands_stack: list):
    """
    the function gets an operators stack and an operands stack, pops the last operator from the stack
     and according to its type, pops operands, calculates the operation and push it to the operands stack
    :param operators_stack: a stack of operators
    :param operands_stack: a stack of operands
    :return: None
    """
    if OPERATIONS.get(operators_stack[-1]).__base__ == OneOperand:
        operand = operands_stack.pop()
        operator = operators_stack.pop()
        operands_stack.append(OPERATIONS.get(operator)(operand).calculate())

    elif OPERATIONS.get(operators_stack[-1]).__base__ == TwoOperands:
        operand2 = operands_stack.pop()
        operand1 = operands_stack.pop()
        operator = operators_stack.pop()
        operands_stack.append(OPERATIONS.get(operator)(operand1, operand2).calculate())


def calculate(arithmetic_expression: str) -> str:
    """
    the function gets an arithmetic expression and calculates it
    :param arithmetic_expression: the arithmetic expression
    :return: the result of the expression
    """
    operands_stack = []
    operators_stack = []
    index = 0
    # loop for scanning the whole expression
    while index < len(arithmetic_expression):
        symbol = arithmetic_expression[index]
        if symbol.isdigit():
            symbol, index = digits_to_number(arithmetic_expression, index)
            operands_stack.append(symbol)
        elif symbol == '(':
            operators_stack.append(symbol)
        elif symbol == ')':
            # loop for scanning the whole expression in the brackets
            while operators_stack.__len__() > 0 and operators_stack[-1] != '(':
                operate_and_push(operators_stack, operands_stack)
            # get rid of (
            operators_stack.pop()
        else:
            # loop for adding the new operator to the correct index in the stack
            while operators_stack.__len__() > 0 and OPERATORS_PRIORITY.get(symbol) < OPERATORS_PRIORITY.get(
                    operators_stack[-1]):
                operate_and_push(operators_stack, operands_stack)
            # push the new operator to the operators stack
            operators_stack.append(symbol)
        index += 1

    # loop for calculating the leftovers
    while operators_stack.__len__() > 0:
        operate_and_push(operators_stack, operands_stack)
    return operands_stack.pop()
