# module for validations on the input
from Brackets.brackets_classes import *
from Operators.operators_classes import *


def validate_pre_calculation(arithmetic_expression: str) -> None:
    """
    this function validates the expression before calculating it
    :param arithmetic_expression: the expression
    :return: None
    """
    if arithmetic_expression == "":
        raise EmptyExpressionError("can't calculate an empty expression!")
    if len(arithmetic_expression) == 1 and not arithmetic_expression[0].isdigit():
        if arithmetic_expression[0] in OPERATORS:
            raise OperandError("can't find operands!")
        else:
            raise UnidentifiedInputError(f"{arithmetic_expression[0]} is unidentified!")


def validate_operator_in_expression(arithmetic_expression: str, index: int) -> None:
    """
    the function validates operator in the received expression
    :param arithmetic_expression: the received expression
    :param index: the index of the operator
    :return: None if the operator is valid, Exception if not
    """
    operator = arithmetic_expression[index]
    if operator not in OPERATORS:
        raise UnidentifiedInputError(f"{operator} is unidentified!")
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
        raise BracketsError(") can't come before (")
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
    elif index < len(arithmetic_expression) - 1:
        if arithmetic_expression[index - 1] in LEFT_UNARY and arithmetic_expression[index + 1] in LEFT_UNARY:
            raise OperatorError(f"{arithmetic_expression[index - 1:index + 2]} sequence is illegal!")
        if (arithmetic_expression[index - 1] in TWO_OPERANDS or arithmetic_expression[index - 1] in OPENERS or
            arithmetic_expression[index - 1] in LEFT_UNARY) and \
                (arithmetic_expression[index + 1] in OPENERS or arithmetic_expression[index + 1] in LEFT_UNARY
                 or validate_right(arithmetic_expression[index + 1], minus)):
            return True
    return False


def validate_tilda_in_minuses(arithmetic_expression: str, index: int) -> bool:
    """
    this function validates tildas sequence in a after or before minus
    :param arithmetic_expression: the expression
    :param index: the index
    :return: True if the sequence is valid
    """
    count_tilda = 0
    while index < len(arithmetic_expression) and \
            (arithmetic_expression[index] == '~' or arithmetic_expression[index] == '-'):
        if arithmetic_expression[index] == '~':
            count_tilda += 1
        if count_tilda > 1:
            raise OperatorError("there is an illegal sequence of tildas!")
        index += 1
    return True


def can_check_after(arithmetic_expression: str, index: int) -> bool:
    """
    the function checks if we can check the index after in the expression
    :param arithmetic_expression: the expression
    :param index: the index
    :return: True if we can, else False
    """
    if index < len(arithmetic_expression) - 1:
        return True
    return False


def can_check_before(index: int) -> bool:
    """
    the function checks if we can check the index before in the expression
    :param index: the index
    :return: True if we can, else False
    """
    if index > 0:
        return True
    return False


def signed_operand(arithmetic_expression: str) -> str:
    """
    this function makes signed minuses in the expression calculable
    :param arithmetic_expression: the arithmetic expression
    :return: the expression after making its signed minuses calculable
    """
    new_expression = ""
    index = 0
    while index < len(arithmetic_expression):
        if arithmetic_expression[index] == '-' and is_signed(arithmetic_expression, index):
            if can_check_after(arithmetic_expression, index):
                if arithmetic_expression[index + 1] in OPENERS or arithmetic_expression[index + 1].isdigit():
                    new_expression += "~"
                    index += 1
                    continue
                if arithmetic_expression[index + 1] == '~' and validate_tilda_in_minuses(arithmetic_expression, index):
                    index += 2
                    continue
        if can_check_after(arithmetic_expression, index) and arithmetic_expression[
            index] == '~' and validate_tilda_in_minuses(arithmetic_expression, index) and \
                arithmetic_expression[index + 1] == '-' and is_signed(
            arithmetic_expression, index + 1):
            index += 2
            continue
        new_expression = new_expression.__add__(arithmetic_expression[index])
        index += 1
    return new_expression
