# module for the system's special operators
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


def digits_sum_util(operand) -> int:
    """
    *this is a utility function for the digits sum '#' operation*
    the function calculates the digits sum of a natural number
    :param operand: the operand
    :return: the sum of the operand's digits
    """
    sum_digits = 0
    while operand > 0:
        sum_digits += operand % 10
        operand //= 10
    return sum_digits


def float_to_integer_util(operand: float) -> int:
    """
    *this is an utility function for the digits sum '#' operation*
    the function converts float into an integer while ignoring the decimal point
    :param operand: operand as float
    :return: operand as int (ignoring the decimal point)
    """
    while not operand.is_integer():
        operand *= 10
    return int(operand)


def digits_sum(operand) -> int:
    """
    the function gets an operand and calculates its digits sum,
    for example:
    6.2 ---> 6+2 ---> 8
    735 ---> 7+3+5 ---> 15
    :param operand: the operand
    :return: the operand's digits sum
    """
    if type(operand) == float:
        if operand < 0:
            operand = negation(operand)
            return negation(digits_sum_util(float_to_integer_util(operand)))
        return digits_sum_util(float_to_integer_util(operand))
    else:
        if operand < 0:
            operand = negation(operand)
            return negation(digits_sum_util(operand))
        return digits_sum_util(operand)
