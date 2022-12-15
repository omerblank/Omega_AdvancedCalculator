from Input.input_calculations import *
from Output.messages import *


def calculation():
    arithmetic_expression = input("Enter something to calculate:\n")
    arithmetic_expression = reduce_spaces(arithmetic_expression)
    arithmetic_expression = reduce_minuses(arithmetic_expression)
    arithmetic_expression = signed_operand(arithmetic_expression)
    if arithmetic_expression == "":
        print("can't calculate an empty expression!")
        calculation()
    # try:
    print(f"Result: {calculate(arithmetic_expression)}")
    # except:
    make_a_choice('c', "CONTINUE", calculation)


def calculator():
    welcome_message()
    calculation()
    goodbye_message()
