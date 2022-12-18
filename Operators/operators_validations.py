# module for operators validations
from ConstantsAndExceptions.constants import *
from ConstantsAndExceptions.exceptions import OperatorError


def validate_left(operand: str, operator) -> bool:
    """
    the function checks if the operand before the operator is a valid operand
    :param operator: the operator
    :param operand: the operand before the operator
    :return: True if the operand is a valid operand,
             else raise ValueError
    """
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        raise ValueError(f"{operand} is illegal before {operator}!")


def validate_right(operand: str, operator) -> bool:
    """
    the function checks if the operand after the operator is a valid operand
    :param operator: the operator
    :param operand: the operand after the operator
    :return: True if the operand is a valid operand,
             else raise ValueError
    """
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        raise ValueError(f"{operand} is illegal after {operator}")


def validate_left_unary(left, right) -> None:
    """
    the function checks if the chars before and after a left unary operator are valid
    :param left: the char before
    :param right: the char after
    :return: None
    """
    if left is not None:
        if (left not in OPERATORS and left not in OPENERS) or left in UNARY:
            raise OperatorError(f"{left} is illegal before {LEFT_UNARY}")
    if right is not None:
        if right not in OPENERS:
            validate_right(right, LEFT_UNARY)


def validate_right_unary(left, right) -> None:
    """
    the function checks if the chars before and after a right unary operator are valid
    :param left: the char before
    :param right: the char after
    :return: None
    """
    if left is not None:
        if left not in CLOSERS and left not in RIGHT_UNARY:
            validate_left(left, RIGHT_UNARY)
    if right is not None:
        if (right not in OPERATORS and right not in CLOSERS) or right in LEFT_UNARY:
            raise OperatorError(f"{right} is illegal after {RIGHT_UNARY}")


def validate_two_operands(left, right) -> None:
    """
    the function checks if the chars before and after a two operands operator are valid
    :param left: the char before
    :param right: the char after
    :return: None
    """
    if (left not in CLOSERS and left not in RIGHT_UNARY) and (right not in OPENERS and right not in LEFT_UNARY):
        validate_left(left, TWO_OPERANDS)
        validate_right(right, TWO_OPERANDS)


def operator_validation(validation, left, right) -> None:
    """
    the function doing a generic validation on an operator
    :param validation: operator validation function - for example: validate_average
    :param left: the char before the operator
    :param right: the char after the operator
    :return: None
    """
    validation(left, right)
