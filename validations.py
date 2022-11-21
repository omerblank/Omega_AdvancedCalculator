from my_exceptions import *


def validate_operand_type(operand) -> bool:
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        print(f"{operand} should be an integer or a float!")


def validate_division(operand2):
    if operand2 == 0:
        raise ZeroDivisionError("Division by zero is illegal!")


def validate_power(operand1, operand2):
    if operand1 == 0 and operand2 == 0:
        raise OperatorError("0 to the power of 0 is illegal!")


def validate_modulo(operand2):
    if operand2 == 0:
        raise ZeroDivisionError("Modulo by zero is illegal!")


def validate_maximum(operand1, operand2):
    if operand1 == operand2:
        raise OperatorError("No maximum between equal operands!")


def validate_minimum(operand1, operand2):
    if operand1 == operand2:
        raise OperatorError("No minimum between equal operands!")


def validate_factorial(operand):
    if (not operand.is_integer()) or operand < 0:
        raise ValueError("Factorial is legal for natural numbers only!")


def two_operands_validation(operator_validation, operand1, operand2):
    operator_validation(operand1, operand2)


def one_operand_validation(operator_validation, operand):
    operator_validation(operand)
