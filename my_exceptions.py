class ParenthesisError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "This is an error related to an incorrect use of parentheses"
