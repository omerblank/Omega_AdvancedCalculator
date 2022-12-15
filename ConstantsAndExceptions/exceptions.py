# module for customized exceptions
class BracketsError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class OperatorError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class OperandError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
