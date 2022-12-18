# module for customized exceptions

# exception for brackets errors
class BracketsError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# exception for operators errors
class OperatorError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
