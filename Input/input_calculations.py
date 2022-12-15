# module for calculations on the input
from Input.input_validations import *
from Operators.operators_classes import *


# utility functions
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
    if OPERATORS_AND_CLASSES.get(operators_stack[-1]).__base__ == OneOperand:
        operand = operands_stack.pop()
        operator = operators_stack.pop()
        if operator in RIGHT_UNARY:
            operands_stack.append(OPERATORS_AND_CLASSES.get(operator)(operand, None).calculate())
        if operator in LEFT_UNARY:
            operands_stack.append(OPERATORS_AND_CLASSES.get(operator)(None, operand).calculate())

    elif OPERATORS_AND_CLASSES.get(operators_stack[-1]).__base__ == TwoOperands:
        operand2 = operands_stack.pop()
        operand1 = operands_stack.pop()
        operator = operators_stack.pop()
        operands_stack.append(OPERATORS_AND_CLASSES.get(operator)(operand1, operand2).calculate())


# main function
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
            validate_bracket_in_expression(arithmetic_expression, index)
            operators_stack.append(symbol)
        elif symbol == ')':
            validate_bracket_in_expression(arithmetic_expression, index)
            # loop for scanning the whole expression in the brackets
            while operators_stack.__len__() > 0 and operators_stack[-1] != '(':
                operate_and_push(operators_stack, operands_stack)
            # get rid of (
            operators_stack.pop()
        else:
            validate_operator_in_expression(arithmetic_expression, index)
            # loop for adding the new operator to the correct index in the stack
            while operators_stack.__len__() > 0 and OPERATORS_PRIORITY.get(symbol) <= OPERATORS_PRIORITY.get(
                    operators_stack[-1]):
                operate_and_push(operators_stack, operands_stack)
            # push the new operator to the operators stack
            operators_stack.append(symbol)
        index += 1

    # loop for calculating the leftovers
    while operators_stack.__len__() > 0:
        operate_and_push(operators_stack, operands_stack)
    return operands_stack.pop()

# def calculation():
#     arithmetic_expression = input("Hi user, please enter something to calculate:\n")
#     arithmetic_expression = reduce_spaces(arithmetic_expression)
#     arithmetic_expression = reduce_minuses(arithmetic_expression)
#     arithmetic_expression = signed_operand(arithmetic_expression)
#     if arithmetic_expression == "":
#         print("can't calculate an empty expression!")
#         calculation()
#     # try:
#     print(f"Result: {calculate(arithmetic_expression)}")
#     choice = input("Press 'Q' to quit Omega Calculator or 'C' to continue:\n")
#     while choice.lower() != 'q' and choice.lower() != 'c':
#         choice = input("Wrong input, Press 'Q' to quit Omega Calculator or 'C' to continue!")
#     if choice.lower() == 'q':
#         print("Ω")
#         pass
#     else:
#         calculation()
#     # except:
