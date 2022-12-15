# module for brackets validations
from ConstantsAndExceptions.constants import *
from ConstantsAndExceptions.exceptions import BracketsError


def validate_round_opener(left, right):
    """
    the function checks if left bracket '(' is valid
    :param left: the char before the bracket
    :param right: the char after the bracket
    :return: None if the bracket is valid, Exception if not
    """
    if left is not None:
        if (left not in OPENERS and left not in OPERATORS) or left in RIGHT_UNARY:
            raise BracketsError(f"{left} can't come before ( !")
    if right is not None:
        if right in RIGHT_UNARY or right in TWO_OPERANDS or right in CLOSERS:
            raise BracketsError(f"{right} can't come after ( !")


def validate_round_closer(left, right):
    """
    the function checks if right bracket ')' is valid
    :param left: the char before the bracket
    :param right: the char after the bracket
    :return: None if the bracket is valid, Exception if not
    """
    if left is not None:
        if left in LEFT_UNARY or left in TWO_OPERANDS or left in OPENERS:
            raise BracketsError(f"{left} can't come before ')' !")
    if right is not None:
        if (right not in CLOSERS and right not in OPERATORS) or right in LEFT_UNARY:
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
