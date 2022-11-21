from my_operators import *
from math import pow


def calculate_addition(operand1, operand2):
    return operand1 + operand2


def calculate_subtraction(operand1, operand2):
    return operand1 - operand2


def calculate_multiplication(operand1, operand2):
    return operand1 * operand2


def calculate_division(operand1, operand2):
    return operand1 / operand2


def calculate_power(operand1, operand2):
    return pow(operand1, operand2)


def calculate_modulo(operand1, operand2):
    return operand1 % operand2


def calculate_maximum(operand1, operand2):
    return maximum(operand1, operand2)


def calculate_minimum(operand1, operand2):
    return minimum(operand1, operand2)


def calculate_average(operand1, operand2):
    return average(operand1, operand2)


def calculate_negation(operand):
    return negation(operand)


def calculate_factorial(operand):
    return factorial(operand)


def two_operands_calculation(operator_calculation, operand1, operand2):
    return operator_calculation(operand1, operand2)


def one_operand_calculation(operator_calculation, operand):
    return operator_calculation(operand)
