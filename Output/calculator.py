# module to show the user the calculator
from Input.input_calculations import *
from Output.messages import *


def get_expression_to_calculate() -> None:
    """
    this function gets the expression from the user and tries to calculate it, final function for calculating
    :return: None
    """
    try:
        arithmetic_expression = input("Enter something to calculate:\n")
        calculation(arithmetic_expression)
    except EOFError as eof:
        print(eof, ", turning calculator OFF!")
        exit(1)
    finally:
        make_a_choice('c', "CONTINUE", get_expression_to_calculate)


def calculation(arithmetic_expression: str):
    """
    the function gets the arithmetic expression, tries to calculate it, and asks the user if he want to insert a new
    input or stop the program
    :param arithmetic_expression: the given expression
    :return: None or Exception
    """
    try:
        print(f"Result: {calculate(arithmetic_expression)}")
        return ()
    except ValueError as ve:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{ve}")
        return ve
    except TypeError as te:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{te}")
        return te
    except ZeroDivisionError as zde:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{zde}")
        return zde
    except OperatorError as oe:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{oe}")
        return oe
    except BracketsError as be:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{be}")
        return be
    except UnidentifiedInputError as uie:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{uie}")
        return uie
    except OperandError as ope:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{ope}")
        return ope
    except EmptyExpressionError as eee:
        print(f"Ω Invalid Expression Entered Ω\n(empty expression)\n{eee}")
        return eee
    except OverflowError as ofe:
        print(f"Ω Invalid Expression Entered Ω\n(the result is too large)\n{ofe}")
        return ofe


def calculator() -> None:
    """
    The function is the total calculator product, including everything in the system
    :return: None
    """
    welcome_message()
    get_expression_to_calculate()
    goodbye_message()
