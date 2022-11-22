from Operators.operators import *

ONE_OPERAND = ['~', '!']
TWO_OPERANDS = ['+', '-', '*', '/', '%', '^', '$', '&', '@']
OPERATORS_PRIORITY = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
OPERATORS = ['+', '-', '*', '/', '%', '^', '$', '&', '@', '~', '!', '(', ')']
OPERATIONS = {'+': Addition, '-': Subtraction, '*': Multiplication, '/': Division, '%': Modulo, '^': Power,
              '$': Maximum, '&': Minimum, '@': Average, '~': Negation, '!': Factorial}
