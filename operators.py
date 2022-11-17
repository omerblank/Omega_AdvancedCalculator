from math import pow


def maximum(operand1, operand2):
    """
    the function gets two operand and returns the greater operand
    :param operand1: first operand
    :param operand2: second operand
    :return: the greater operand
    """
    # check operands validity
    if operand1 == operand2:
        raise ValueError("Operands are equal, there is not a maximum!")

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
    # check operands validity
    if operand1 == operand2:
        raise ValueError("Operands are equal, there is not a minimum!")

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


# utility function
def is_integer(operand: float) -> bool:
    """
    the function gets a float and returns True is its an int:
    for example: is_integer(6.0)->True
                 is_integer(6.3)->False
    :param operand: the operand
    :return: True if the operand is an int, else False.
    """
    if operand == 0:
        return True
    elif operand > 0:
        while operand > 0:
            operand -= 1
            if operand == 0:
                return True
        return False
    else:
        while operand < 0:
            operand += 1
            if operand == 0:
                return True
        return False


def factorial(operand: int) -> int:
    """
    the function gets an operand and returns its factorial
    :param operand: operand
    :return: the factorial of the operand
    """
    if type(operand) != int and not is_integer(operand):
        raise TypeError("Factorial works only on natural operand or zero!")
    if operand < 0:
        raise ValueError("Factorial works only on natural operand or zero!")
    final_factorial = 1
    while operand > 0:
        final_factorial *= operand
        operand -= 1
    return int(final_factorial)


def two_operands(operand1, operand2, operator: str):
    """
    the function gets 2 operands:
    operand1 from type float or int
    operand2 from type float or int
    and an operator from type str:
    +: addition
    -: subtraction
    *: multiplication
    /: division
    ^: power
    %: modulo
    $: maximum
    &: minimum
    @: average
    :param operand1: first operand
    :param operand2: second operand
    :param operator: operator
    :return: the operation result
    """
    # check input type
    if type(operator) != str:
        raise TypeError("Operator should be a string!")
    if type(operand1) != int and type(operand1) != float:
        raise TypeError("Operand1 should be a int or a float!")
    if type(operand2) != int and type(operand2) != float:
        raise TypeError("Operand2 should be a int or a float!")

    # check input value
    if operator == '!' or operator == '~':
        raise ValueError(f"{operator} can only operate on one operand!")
    if operator != '+' and operator != '-' and operator != '*' and operator != '/' and operator != '^' and operator != '%' and operator != '$' and operator != '&' and operator != '@':
        raise ValueError(f"{operator} is not an operator!")

    if operator == '+':
        return operand1 + operand2

    elif operator == '-':
        return operand1 - operand2

    elif operator == '*':
        return operand1 * operand2

    elif operator == '/':
        # division in python handles the case of division by zero so we do not have to handle it
        return operand1 / operand2

    elif operator == '^':
        # check input value
        # math pow does not handles the case of zero to the power of zero
        if operand1 == 0 and operand2 == 0:
            raise ValueError("0 to the power of 0 is undefined!")
        # math pow handles the case of a negative number square root so we do not have to handle it

        return pow(operand1, operand2)

    elif operator == '%':
        return operand1 % operand2

    elif operator == '$':
        return maximum(operand1, operand2)

    elif operator == '&':
        return minimum(operand1, operand2)

    elif operator == '@':
        return average(operand1, operand2)


def single_operand(operand, operator: str):
    """
    the function gets an operand from type int or float
    and an operator from type str:
    ~: negation
    !: factorial
    :param operand: operand
    :param operator: operator
    :return: the operation result
    """
    # check input type
    if type(operator) != str:
        raise TypeError("Operator should be a string!")
    if type(operand) != int and type(operand) != float:
        raise TypeError("Operand should be a int or a float!")

    # check input value
    if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '^' or operator == '%' or operator == '$' or operator == '&' or operator == '@':
        raise ValueError(f"{operator} can only operate on two operands!")
    if operator != '~' and operator != '!':
        raise ValueError(f"{operator} is not an operator!")

    if operator == '~':
        return negation(operand)

    elif operator == '!':
        return factorial(operand)
#check!