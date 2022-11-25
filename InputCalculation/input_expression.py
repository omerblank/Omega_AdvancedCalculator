from InputCalculation.calculate_expression import *


class Expression(object):
    def __init__(self, arithmetic_expression: str):
        self.expression = arithmetic_expression

    def handle_expression(self):
        pass

    def calculate(self):
        return calculate(self.expression)
