from constants import *


def infix_to_postfix(arithmetic_expression: str) -> str:
    stack = []
    postfix_expression = ""
    index = 0
    while index < len(arithmetic_expression):
        symbol = arithmetic_expression[index]
        if symbol.isdigit():
            symbol = int(symbol)
            while index + 1 != len(arithmetic_expression) and arithmetic_expression[index + 1].isdigit():
                symbol *= 10
                symbol += int(arithmetic_expression[index + 1])
                index += 1
            postfix_expression += str(symbol)
        else:
            if symbol == '(':
                stack.append(symbol)
            else:
                if symbol == ')':
                    while stack.__len__() > 0 and stack[-1] != '(':
                        postfix_expression += stack.pop()
                    stack.pop()
                else:
                    while stack.__len__() > 0 and OPERATORS_PRIORITY.get(symbol) < OPERATORS_PRIORITY.get(stack[-1]):
                        postfix_expression += stack.pop()
                    stack.append(symbol)
        index += 1
    while stack.__len__() > 0:
        postfix_expression += stack.pop()
    return postfix_expression
