from Operators.operators_classes import *
from Brackets.brackets_classes import *

ONE_OPERAND = {'~': "left", '!': "right", '#': "right"}
TWO_OPERANDS = ['+', '-', '*', '/', '%', '^', '$', '&', '@']
OPERATORS_PRIORITY = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6,
                      '#': 6}
OPERATORS = {'+': Addition, '-': Subtraction, '*': Multiplication, '/': Division, '%': Modulo, '^': Power,
             '$': Maximum, '&': Minimum, '@': Average, '~': Negation, '!': Factorial, '#': DigitsSum}
BRACKETS = {'(': RoundLeftBracket, ')': RoundRightBracket}
OPERANDS_FOR_OPERATOR = {OneOperand: 1, TwoOperands: 2}
