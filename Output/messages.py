# module to show the user messages while he is using the calculator
from Input.input_validations import *


def make_a_choice(valid_choice: str, do_what: str, operation) -> None:
    """
    this function asks the user if he wants to make a choice or not
    :param valid_choice: the input for making the choice
    :param do_what: what the choice will do
    :param operation: the function that the choice will operate
    :return: None
    """
    choice = input(f"Ω PRESS '{valid_choice}' TO {do_what} OR ENTER TO SKIP Ω\n")
    while choice.lower() != valid_choice and choice != '':
        choice = input(f"Ω INVALID INPUT, PRESS '{valid_choice}' TO {do_what} OR ENTER TO SKIP Ω\n")
    if choice.lower() == valid_choice:
        operation()
    print()


def make_a_choice_with_feature(valid_choice, do_what, operation, feature) -> None:
    """
    this function asks the user if he wants to make a choice or not
    :param valid_choice: the input for making the choice
    :param do_what: what the choice will do
    :param operation: the function that the choice will operate
    :param feature: the function that the operation function will operate
    :return: None
    """
    choice = input(f"Ω PRESS '{valid_choice}' TO {do_what} OR ENTER TO SKIP Ω\n")
    while choice.lower() != valid_choice and choice != '':
        choice = input(f"Ω INVALID INPUT, PRESS '{valid_choice}' TO {do_what} OR ENTER TO SKIP Ω\n")
    if choice.lower() == valid_choice:
        operation(feature)
    print()


def try_me(feature) -> None:
    """
    this function let the user to try a feature in the calculator
    :param feature: the feature to try
    :return: None
    """
    expression = input("Ω ENTER AN ARITHMETIC EXPRESSION Ω\n")
    print(f"Ω AFTER FEATURE Ω\n{feature(expression)}")


def minuses_reducing_feature() -> None:
    """
    this function introduce the minus reducing function to the user, and allows him to try it
    :return: None
    """
    print("Ω MINUS REDUCING FEATURE Ω\n"
          "this feature allows you to enter as many minuses as you want between operators or between "
          "operands.\n"
          "the system takes care of reducing the minuses accordingly.\n")
    make_a_choice_with_feature('-', "TRY ME", try_me, reduce_minuses)


def spaces_reducing_feature() -> None:
    """
    this function introduce the spaces reducing function to the user, and allows him to try it
    :return: None
    """
    print("Ω SPACES REDUCING FEATURE Ω\n"
          "this feature allows you to enter as many spaces as you want everywhere.\n"
          "the system takes care of reducing the spaces accordingly.\n")
    make_a_choice_with_feature(' ', "TRY ME", try_me, reduce_spaces)


def introduce_features() -> None:
    """
    this function introduces the features of the system to the user
    :return: None
    """
    minuses_reducing_feature()
    spaces_reducing_feature()


def introduce_operators() -> None:
    """
    this function introduces the operators of the system to the user
    :return: None
    """
    print(f"Ω OPERATORS FOR TWO OPERANDS Ω\n"
          f"{TWO_OPERANDS}\n"
          f"Ω OPERATORS FOR ONE OPERAND Ω\n"
          f"Ω RIGHT UNARY OPERATORS (appear to the right of an operand) Ω\n"
          f"{RIGHT_UNARY}\n"
          f"Ω LEFT UNARY OPERATORS (appear to the left of an operand) Ω\n"
          f"{RIGHT_UNARY}\n"
          f"Ω OPERATORS PRIORITY Ω\n"
          f"{OPERATORS_PRIORITY}")


def welcome_message() -> None:
    """
    function for welcoming the user
    :return: None
    """
    print("Ω WELCOME TO OMEGA CALCULATOR! Ω\n"
          "in this calculator, OPERAND is an arithmetic expression, for example:\n"
          "1) 2\n"
          "2) 2.3\n"
          "3) (2+3)\n")
    make_a_choice('o', "SEE AVAILABLE OPERATORS", introduce_operators)
    make_a_choice('f', "SEE AVAILABLE FEATURES", introduce_features)
    print("Ω ENJOY! Ω\n")


def goodbye_message() -> None:
    """
    function for saying goodbye to the user
    :return: None
    """
    print("Ω See you soon! Ω")
