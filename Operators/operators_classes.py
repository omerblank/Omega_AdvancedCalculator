from Operators.operators_calculations import *
from Operators.operators_validations import *


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



