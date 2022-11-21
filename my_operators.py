def maximum(operand1, operand2):
    """
    the function gets two operand and returns the greater operand
    :param operand1: first operand
    :param operand2: second operand
    :return: the greater operand
    """
    if operand1 > operand2:
        return operand1
    return operand2


def minimum(operand1, operand2):
    """
    the function gets two operand and returns the lower operand
    :param operand1: first operand
    :param operand2: second operand
    :return: the lower operand
    """
    if operand1 < operand2:
        return operand1
    return operand2


def average(operand1, operand2):
    """
    the function gets two operands and returns the average of them
    :param operand1: first operand
    :param operand2: second operand
    :return: the average
    """
    return (operand1 + operand2) / 2


def negation(operand):
    """
    the function gets an operand and returns its negation result
    :param operand: operand
    :return: the negation result
    """
    return -operand


def factorial(operand: int) -> int:
    """
    the function gets an operand and returns its factorial
    :param operand: operand
    :return: the factorial of the operand
    """
    final_factorial = 1
    while operand > 0:
        final_factorial *= operand
        operand -= 1
    return int(final_factorial)
