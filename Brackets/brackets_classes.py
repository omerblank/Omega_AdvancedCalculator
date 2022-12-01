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
        super().validate(validate_left_bracket)


class RoundRightBracket(Bracket):
    def __init__(self, left, right):
        super().__init__(left, right)
        super().validate(validate_right_bracket)
