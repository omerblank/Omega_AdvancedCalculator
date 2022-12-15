from ConstantsAndExceptions.constants import *
from ConstantsAndExceptions.exceptions import OperatorError
from Operators.operators_calculations import *


class Operator(object):
    def validate(self, validation):
        pass

    def calculate(self, operator_calculation):
        pass


class OneOperand(Operator):
    def __init__(self, left, right, operand):
        self.left = left
        self.right = right
        self.operand = operand

    def validate(self, validation):
        return operator_validation(validation, self.left, self.right)

    def calculate(self, operator_calculation):
        return one_operand_calculation(operator_calculation, self.operand)


class TwoOperands(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def validate(self, validation):
        return operator_validation(validation, self.left, self.right)

    def calculate(self, operator_calculation):
        return two_operands_calculation(operator_calculation, self.left, self.right)


class Addition(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_addition)

    def calculate(self):
        return super().calculate(calculate_addition)


class Subtraction(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_subtraction)

    def calculate(self):
        return super().calculate(calculate_subtraction)


class Multiplication(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_multiplication)

    def calculate(self):
        return super().calculate(calculate_multiplication)


class Division(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_division)

    def calculate(self):
        return super().calculate(calculate_division)


class Power(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_power)

    def calculate(self):
        return super().calculate(calculate_power)


class Modulo(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_modulo)

    def calculate(self):
        return super().calculate(calculate_modulo)


class Maximum(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_maximum)

    def calculate(self):
        return super().calculate(calculate_maximum)


class Minimum(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_minimum)

    def calculate(self):
        return super().calculate(calculate_minimum)


class Average(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_average)

    def calculate(self):
        return super().calculate(calculate_average)


class Negation(OneOperand):
    def __init__(self, left, right):
        super().__init__(left, right, right)
        super().validate(validate_negation)

    def calculate(self):
        return super().calculate(calculate_negation)


class Factorial(OneOperand):
    def __init__(self, left, right):
        super().__init__(left, right, left)
        super().validate(validate_factorial)

    def calculate(self):
        return super().calculate(calculate_factorial)


class DigitsSum(OneOperand):
    def __init__(self, left, right):
        super().__init__(left, right, left)
        super().validate(validate_digits_sum)

    def calculate(self):
        return super().calculate(calculate_digits_sum)


# Operators Constants:
OPERATORS = {'+': Addition, '-': Subtraction, '*': Multiplication, '/': Division, '%': Modulo, '^': Power,
             '$': Maximum, '&': Minimum, '@': Average, '~': Negation, '!': Factorial, '#': DigitsSum}
OPERANDS_FOR_OPERATOR = {OneOperand: 1, TwoOperands: 2}


# Operators Validations:
def validate_left(operand: str, operator) -> bool:
    """
    the function checks if the left char is operand
    :param operator: the operator to validate
    :param operand: the char
    :return: True if the operand is an operand
             except ValueError if the char is not an operand
    """
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        raise ValueError(f"{operand} is illegal before {operator}!")


def validate_right(operand: str, operator) -> bool:
    """
    the function checks if the right char is operand
    :param operator: the operator to validate
    :param operand: the char
    :return: True if the operand is an operand
             except ValueError if the char is not an operand
    """
    try:
        return type(int(operand)) == int or type(float(operand)) == float
    except ValueError:
        raise ValueError(f"{operand} is illegal after {operator}")


def validate_left_unary(left, right):
    if left is not None:
        if (left not in OPERATORS and left not in OPENERS) or left in UNARY:
            raise OperatorError(f"{left} is illegal before {LEFT_UNARY}")
    if right is not None:
        if right not in OPENERS:
            validate_right(right, LEFT_UNARY)


def validate_right_unary(left, right):
    if left is not None:
        if left not in CLOSERS and left not in RIGHT_UNARY:
            validate_left(left, RIGHT_UNARY)
    if right is not None:
        if (right not in OPERATORS and right not in CLOSERS) or right in LEFT_UNARY:
            raise OperatorError(f"{right} is illegal after {RIGHT_UNARY}")


def validate_two_operands(left, right):
    """
    the function checks if two operands are numbers
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operands are numbers
             except ValueError if the one or more of the operands is not a number
    """
    if (left not in CLOSERS and left not in RIGHT_UNARY) and (right not in OPENERS and right not in LEFT_UNARY):
        validate_left(left, TWO_OPERANDS)
        validate_right(right, TWO_OPERANDS)


def validate_addition(left, right):
    """
    the function checks if addition operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)


def validate_subtraction(left, right):
    """
    the function checks if subtraction operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)


def validate_multiplication(left, right):
    """
    the function checks if multiplication operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)


def validate_division(left, right):
    """
    the function checks if division operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)
    # if right == 0:
    #     raise ZeroDivisionError("Division by zero is illegal!")


def validate_power(left, right):
    """
    the function checks if power operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)
    # if left == 0 and right == 0:
    #     raise OperatorError("0 to the power of 0 is illegal!")


def validate_modulo(left, right):
    """
    the function checks if modulo operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)
    # if right == 0:
    #     raise ZeroDivisionError("Modulo by zero is illegal!")


def validate_maximum(left, right):
    """
    the function checks if maximum operation is valid
    :param left: the char before the operator (supposed to be an operand)
    :param right: the char after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)
    # if left == right:
    #     raise OperatorError("No maximum between equal operands!")


def validate_minimum(left, right):
    """
    the function checks if minimum operation is valid
    :param left: the operand before the operator (supposed to be an operand)
    :param right: the operand after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)
    # if left == right:
    #     raise OperatorError("No minimum between equal operands!")


def validate_average(left, right):
    """
    the function checks if average operation is valid
    :param left: the operand before the operator (supposed to be an operand)
    :param right: the operand after the operator (supposed to be an operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_two_operands(left, right)


def validate_negation(left, right):
    """
    the function checks if negation operation is valid
    :param left: the operand before the operator
    :param right: the operand after the operator (supposed to be the operand)
    :return: None if the operation is valid, Exception if not
    """
    validate_left_unary(left, right)


def validate_factorial(left, right):
    """
    the function checks if factorial operation is valid
    :param left: the operand before the operator (supposed to be the operand)
    :param right: the operand after the operator
    :return: None if the operation is valid, Exception if not
    """
    validate_right_unary(left, right)
    # if not float(left).is_integer() or int(left) < 0:
    #     raise ValueError("Factorial is legal for natural numbers only!")


def validate_digits_sum(left, right):
    """
    the function checks if digits sum operation is valid
    :param left: the operand before the operator (supposed to be the operand)
    :param right: the operand after the operator
    :return: None if the operation is valid, Exception if not
    """
    validate_right_unary(left, right)


def operator_validation(validation, left, right):
    """
    the function doing a generic validation on an operator
    :param validation: operator validation function - for example: validate_average
    :param left: the operand before the operator
    :param right: the operand after the operator
    :return: None if the operation is valid, Exception if not
    """
    validation(left, right)
