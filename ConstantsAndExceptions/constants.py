# module for general constants
OPERATORS = ['+', '-', '*', '/', '%', '^', '$', '&', '@', '!', '~', '#']
TWO_OPERANDS = ['+', '-', '*', '/', '%', '^', '$', '&', '@']
UNARY = ['!', '~', '#']
RIGHT_UNARY = ['!', '#']
LEFT_UNARY = ['~']
OPERATORS_PRIORITY = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6,
                      '#': 6}
BRACKETS = ['(', ')']
OPENERS = ['(']
CLOSERS = [')']
IGNORE = [' ', '\t', '\n']
