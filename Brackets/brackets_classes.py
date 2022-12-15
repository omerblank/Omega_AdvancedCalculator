# module for brackets classes
from Brackets.brackets_validations import *


class Bracket(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def validate(self, validation):
        return bracket_validation(validation, self.left, self.right)


class RoundLeftBracket(Bracket):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_round_opener)


class RoundRightBracket(Bracket):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_round_closer)


# Brackets Constants:
BRACKETS_AND_CLASSES = {'(': RoundLeftBracket, ')': RoundRightBracket}

# Brackets Validations:
