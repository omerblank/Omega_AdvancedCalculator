# module for operators classes
from Operators.operators_calculations import *
from Operators.operators_validations import *


# class for general operator (a base)
class Operator(object):
    def validate(self) -> None:
        """
        the function does a validation for the operands that are next to the operator
        (depends on the type of the operator)
        :return: None
        """
        pass

    def calculate(self, operator_calculation):
        """
        the function does a calculation for an operator if it's valid
        :param operator_calculation: the calculation (depends on the type of the operator)
        :return: None
        """
        pass


# class for a general left unary operator (a base)
class LeftUnary(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def validate(self):
        return operator_validation(validate_left_unary, self.left, self.right)

    def calculate(self, operator_calculation):
        return one_operand_calculation(operator_calculation, self.right)


# class for a general right unary operator (a base)
class RightUnary(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def validate(self):
        return operator_validation(validate_right_unary, self.left, self.right)

    def calculate(self, operator_calculation):
        return one_operand_calculation(operator_calculation, self.left)


# class for a general two operands operator (a base)
class TwoOperands(Operator):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def validate(self):
        return operator_validation(validate_two_operands, self.left, self.right)

    def calculate(self, operator_calculation):
        return two_operands_calculation(operator_calculation, self.left, self.right)


# class for Addition operator ('+')
class Addition(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_addition)


# class for Subtraction operator ('-')
class Subtraction(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_subtraction)


# class for Multiplication operator ('*')
class Multiplication(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_multiplication)


# class for Division operator ('/')
class Division(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_division)


# class for Power operator ('^')
class Power(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_power)


# class for Modulo operator ('%')
class Modulo(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_modulo)


# class for Maximum operator ('$')
class Maximum(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_maximum)


# class for Minimum operator ('&')
class Minimum(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_minimum)


# class for Average operator ('@')
class Average(TwoOperands):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_average)


# class for Negation operator ('~')
class Negation(LeftUnary):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_negation)


# class for Factorial operator ('!')
class Factorial(RightUnary):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_factorial)


# class for DigitsSum operator ('#')
class DigitsSum(RightUnary):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate()

    def calculate(self):
        return super().calculate(calculate_digits_sum)


# Operators classes Constants:
OPERATORS_AND_CLASSES = {'+': Addition, '-': Subtraction, '*': Multiplication, '/': Division, '%': Modulo, '^': Power,
                         '$': Maximum, '&': Minimum, '@': Average, '~': Negation, '!': Factorial, '#': DigitsSum}
