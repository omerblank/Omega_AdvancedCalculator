from my_exceptions import *


def validate_operand_type(operand) -> bool:
    """
    the function checking if operand is a number
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
    the function checking if two operands are numbers
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operands are numbers
             except ValueError if the one or more of the operands is not a number
    """
    validate_operand_type(operand1)
    validate_operand_type(operand2)


def validate_addition(operand1, operand2):
    """
    the function check if addition operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)


def validate_subtraction(operand1, operand2):
    """
    the function check if subtraction operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)


def validate_multiplication(operand1, operand2):
    """
    the function check if multiplication operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)


def validate_division(operand1, operand2):
    """
    the function check if division operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)
    if operand2 == 0:
        raise ZeroDivisionError("Division by zero is illegal!")


def validate_power(operand1, operand2):
    """
    the function check if power operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)
    if operand1 == 0 and operand2 == 0:
        raise OperatorError("0 to the power of 0 is illegal!")


def validate_modulo(operand1, operand2):
    """
    the function check if modulo operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)
    if operand2 == 0:
        raise ZeroDivisionError("Modulo by zero is illegal!")


def validate_maximum(operand1, operand2):
    """
    the function check if maximum operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)
    if operand1 == operand2:
        raise OperatorError("No maximum between equal operands!")


def validate_minimum(operand1, operand2):
    """
    the function check if minimum operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)
    if operand1 == operand2:
        raise OperatorError("No minimum between equal operands!")


def validate_average(operand1, operand2):
    """
    the function check if average operation is valid
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands_type(operand1, operand2)


def validate_negation(operand):
    """
    the function check if negation operation is valid
    :param operand: the operand
    :return: None if the operation is valid, Exception if not
    """
    validate_operand_type(operand)


def validate_factorial(operand):
    """
    the function check if factorial operation is valid
    :param operand: the operand
    :return: None if the operation is valid, Exception if not
    """
    validate_operand_type(operand)
    if (not operand.is_integer()) or operand < 0:
        raise ValueError("Factorial is legal for natural numbers only!")


def validate_left_bracket(operand):
    validate_operand_type(operand)


def validate_right_bracket(operand):
    validate_operand_type(operand)


def two_operands_validation(operator_validation, operand1, operand2):
    """
    the function doing a generic validation on operand1 and operand2
    :param operator_validation: two operands operator validation function - for example: validate_average
    :param operand1: first operand
    :param operand2: second operand
    :return: None if the operation is valid, Exception if not
    """
    operator_validation(operand1, operand2)


def one_operand_validation(operator_validation, operand):
    """
    the function doing a generic validation on operand
    :param operator_validation: one operand operator validation function - for example: validate_factorial
    :param operand: the operand
    :return: None if the operation is valid, Exception if not
    """
    operator_validation(operand)
