from Operators.validations import *
from Operators.calculations import *


class Operator(object):
    def validate(self, operator_validation):
        pass

    def calculate(self, operator_calculation):
        pass


class OneOperand(Operator):
    def __init__(self, operand):
        self.operand = operand

    def validate(self, operator_validation):
        return one_operand_validation(operator_validation, self.operand)

    def calculate(self, operator_calculation):
        return one_operand_calculation(operator_calculation, self.operand)


class TwoOperands(Operator):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def validate(self, operator_validation):
        return two_operands_validation(operator_validation, self.operand1, self.operand2)

    def calculate(self, operator_calculation):
        return two_operands_calculation(operator_calculation, self.operand1, self.operand2)


class Addition(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_addition)

    def calculate(self):
        return super().calculate(calculate_addition)


class Subtraction(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_subtraction)

    def calculate(self):
        return super().calculate(calculate_subtraction)


class Multiplication(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_multiplication)

    def calculate(self):
        return super().calculate(calculate_multiplication)


class Division(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_division)

    def calculate(self):
        return super().calculate(calculate_division)


class Power(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_power)

    def calculate(self):
        return super().calculate(calculate_power)


class Modulo(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_modulo)

    def calculate(self):
        return super().calculate(calculate_modulo)


class Maximum(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_maximum)

    def calculate(self):
        return super().calculate(calculate_maximum)


class Minimum(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_minimum)

    def calculate(self):
        return super().calculate(calculate_minimum)


class Average(TwoOperands):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)
        super().validate(validate_average)

    def calculate(self):
        return super().calculate(calculate_average)


class Negation(OneOperand):
    def __init__(self, operand):
        super().__init__(operand)
        super().validate(validate_negation)

    def calculate(self):
        return super().calculate(calculate_negation)


class Factorial(OneOperand):
    def __init__(self, operand):
        super().__init__(operand)
        super().validate(validate_factorial)

    def calculate(self):
        return super().calculate(calculate_factorial)


class LeftBracket(OneOperand):
    def __init__(self, operand):
        super().__init__(operand)
        super().validate(validate_left_bracket)


class RightBracket(OneOperand):
    def __init__(self, operand):
        super().__init__(operand)
        super().validate(validate_right_bracket())
