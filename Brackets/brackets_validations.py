from ConstantsAndExceptions.constants import *
from ConstantsAndExceptions.exceptions import BracketsError


def validate_left_bracket(left, right):
    """
    the function checks if left bracket '(' is valid
    :param left: the char before the bracket
    :param right: the char after the bracket
    :return: None if the bracket is valid, Exception if not
    """
    if left is not None:
        if left not in OPERATORS or ONE_OPERAND.get(left) == "right":
            raise BracketsError(f"{left} can't come before '(' !")
    if right is not None:
        if ONE_OPERAND.get(right) == "right" or (right in TWO_OPERANDS and right != '-'):
            raise BracketsError(f"{right} can't come after '(' !")


def validate_right_bracket(left, right):
    """
    the function checks if right bracket ')' is valid
    :param left: the char before the bracket
    :param right: the char after the bracket
    :return: None if the bracket is valid, Exception if not
    """
    if left is not None:
        if ONE_OPERAND.get(left) == "left" or (left in TWO_OPERANDS):
            raise BracketsError(f"{left} can't come before ')' !")
    if right is not None:
        if right not in OPERATORS or ONE_OPERAND.get(right) == "right":
            raise BracketsError(f"{right} can't come after ')' !")


def bracket_validation(validation, left, right):
    """
    the function doing a generic validation on a bracket
    :param validation: bracket validation function - for example: validate_right_bracket
    :param left: the char before the operator
    :param right: the char after the operator
    :return: None if the bracket is valid, Exception if not
    """
    validation(left, right)
