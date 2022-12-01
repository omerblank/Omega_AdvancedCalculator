from InputCalculation.calculate_expression import *
from InputCalculation.input_validations import *


class Expression(object):
    def __init__(self, arithmetic_expression: str):
        self.expression = arithmetic_expression

    def handle_expression(self):
        self.expression = reduce_minuses(self.expression)
        print(self.expression)

    def calculate(self):
        return calculate(self.expression)
