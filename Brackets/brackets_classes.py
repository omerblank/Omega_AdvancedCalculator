# module for brackets classes
from Brackets.brackets_validations import *


# class for general bracket (a base)
class Bracket(object):
    def __init__(self, left, right):
        """
        function for initializing a bracket object
        :param left: the operand from the left of the bracket
        :param right: the operand from the right of the bracket
        """
        self.left = left
        self.right = right

    def validate(self, validation) -> None:
        """
        the function does a validations on the operands that are next to the bracket
        :param validation: the validation (depends on the type of the bracket)
        :return: None
        """
        return bracket_validation(validation, self.left, self.right)


# class for a round left bracket ('(')
class RoundLeftBracket(Bracket):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_round_opener)


# class for a round right bracket (')')
class RoundRightBracket(Bracket):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_round_closer)


# Brackets Constants:
BRACKETS_AND_CLASSES = {'(': RoundLeftBracket, ')': RoundRightBracket}
