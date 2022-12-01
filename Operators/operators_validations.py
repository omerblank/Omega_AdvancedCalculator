from ConstantsAndExceptions.constants import *
from ConstantsAndExceptions.exceptions import *


def validate_operand_type(operand) -> bool:
    """
    the function checks if operand is a number
    :param operand: the operand
    :return: True if the operand is a number
             except ValueError if the operand is not a number
    """
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        print(f"{operand} should be an integer or a float!")


def validate_two_operands_type(operand1, operand2):
    """
    the function checks if two operands are numbers
    :param operand1: the char before the operator (supposed to be an operand)
    :param operand2: the char after the operator (supposed to be an operand)
    :return: None if the operands are numbers
             except ValueError if the one or more of the operands is not a number
    """
    validate_operand_type(operand1)
    validate_operand_type(operand2)


def validate_addition(left, right):
    """
    the function checks if addition operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)


def validate_subtraction(left, right):
    """
    the function checks if subtraction operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)


def validate_multiplication(left, right):
    """
    the function checks if multiplication operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)


def validate_division(left, right):
    """
    the function checks if division operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)
    if right == 0:
        raise ZeroDivisionError("Division by zero is illegal!")


def validate_power(left, right):
    """
    the function checks if power operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)
    if left == 0 and right == 0:
        raise OperatorError("0 to the power of 0 is illegal!")


def validate_modulo(left, right):
    """
    the function checks if modulo operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)
    if right == 0:
        raise ZeroDivisionError("Modulo by zero is illegal!")


def validate_maximum(left, right):
    """
    the function checks if maximum operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)
    if left == right:
        raise OperatorError("No maximum between equal operands!")


def validate_minimum(left, right):
    """
    the function checks if minimum operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)
    if left == right:
        raise OperatorError("No minimum between equal operands!")


def validate_average(left, right):
    """
    the function checks if average operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(left, right)


def validate_negation(left, right):
    """
    the function checks if negation operation is valid
    :param left: the char before the operator
    :param right: the char after the operator (supposed to be the operand)
    :return: None if the operation is valid, Exception if not
    """
    if left is not None:
        if left not in OPERATORS:
            raise OperatorError("There should be an operator on the left of negation operator!")
    if right is not None:
        validate_operand_type(right)


def validate_factorial(left, right):
    """
    the function checks if factorial operation is valid
    :param left: the char before the operator (supposed to be the operand)
    :param right: the char after the operator
    :return: None if the operation is valid, Exception if not
    """
    if left is not None:
        validate_operand_type(left)
        if not float(left).is_integer() or int(left) < 0:
            raise ValueError("Factorial is legal for natural numbers only!")
    if right is not None:
        if right not in OPERATORS:
            raise OperatorError("There should be an operator on the left of negation operator!")


def validate_digits_sum(left, right):
    """
    the function checks if digits sum operation is valid
    :param left: the char before the operator (supposed to be the operand)
    :param right: the char after the operator
    :return: None if the operation is valid, Exception if not
    """
    if left is not None:
        validate_operand_type(left)
    if right is not None:
        if right not in OPERATORS:
            raise OperatorError("There should be an operator on the left of negation operator!")


def operator_validation(validation, left, right):
    """
    the function doing a generic validation on an operator
    :param validation: operator validation function - for example: validate_average
    :param left: the char before the operator
    :param right: the char after the operator
    :return: None if the operation is valid, Exception if not
    """
    validation(left, right)
