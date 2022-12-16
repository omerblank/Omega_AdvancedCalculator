# module to show the user the calculator
from Input.input_calculations import *
from Output.messages import *


def calculation() -> None:
    """
    the function gets the input from the user, tries to calculate it, and asks the user if he want to insert a new
    input or stop the program
    :return: None
    """
    try:
        arithmetic_expression = input("Enter something to calculate:\n")
    except EOFError as eof:
        print(eof, ", turning calculator OFF!")
        return
    arithmetic_expression = reduce_spaces(arithmetic_expression)
    arithmetic_expression = reduce_minuses(arithmetic_expression)
    arithmetic_expression = signed_operand(arithmetic_expression)
    if arithmetic_expression == "":
        print("can't calculate an empty expression!")
        calculation()
    try:
        print(f"Result: {calculate(arithmetic_expression)}")
    except ValueError as ve:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{ve}")
    except TypeError as te:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{te}")
    except ZeroDivisionError as zde:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{zde}")
    except OperatorError as oe:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{oe}")
    except BracketsError as be:
        print(f"Ω Invalid Expression Entered Ω\n{arithmetic_expression}\n{be}")
    finally:
        make_a_choice('c', "CONTINUE", calculation)


def calculator() -> None:
    """
    The function is the total calculator product, including everything in the system
    :return: None
    """
    welcome_message()
    calculation()
    goodbye_message()
