from Operators.my_operators import *
from math import pow


def calculate_addition(operand1, operand2):
    """"
    the function doing addition operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 + operand2
    """
    return operand1 + operand2


def calculate_subtraction(operand1, operand2):
    """
    the function doing subtraction operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 - operand2
    """
    return operand1 - operand2


def calculate_multiplication(operand1, operand2):
    """
    the function doing multiplication operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 * operand2
    """
    return operand1 * operand2


def calculate_division(operand1, operand2):
    """
    the function doing division operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 / operand2
    """
    return operand1 / operand2


def calculate_power(operand1, operand2):
    """
    the function doing power operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 ^ operand2
    """
    return pow(operand1, operand2)


def calculate_modulo(operand1, operand2):
    """
    the function doing modulo operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 % operand2
    """
    return operand1 % operand2


def calculate_maximum(operand1, operand2):
    """
    the function doing maximum operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 $ operand2
    """
    return maximum(operand1, operand2)


def calculate_minimum(operand1, operand2):
    """
    the function doing minimum operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 & operand2
    """
    return minimum(operand1, operand2)


def calculate_average(operand1, operand2):
    """
    the function doing average operation on operand1 and operand2
    :param operand1: first operand
    :param operand2: second operand
    :return: operand1 @ operand2
    """
    return average(operand1, operand2)


def calculate_negation(operand):
    """
    the function doing negation operation on operand
    :param operand: the operand
    :return: ~operand
    """
    return negation(operand)


def calculate_factorial(operand):
    """
    the function doing factorial operation on operand
    :param operand: the operand
    :return: operand!
    """
    return factorial(operand)

def two_operands_calculation(operator_calculation, operand1, operand2):
    """
    the function doing a generic calculation on operand1 and operand2
    :param operator_calculation: two operands operator calculation function - for example: calculate_average
    :param operand1: first operand
    :param operand2: second operand
    :return: operator_calculation(operand1, operand2)
    """
    return operator_calculation(operand1, operand2)


def one_operand_calculation(operator_calculation, operand):
    """
    the function doing a generic calculation on operand
    :param operator_calculation: one operand operator calculation function - for example: calculate_factorial
    :param operand: the operand
    :return: operator_calculation(operand)
    """
    return operator_calculation(operand)
