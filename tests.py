import pytest
from ConstantsAndExceptions.exceptions import *
from Output.calculator import calculation


def test_simple_errors():
    exception = calculation("(2+3))")
    assert isinstance(exception, BracketsError)

    exception = calculation("13..4+0.6")
    assert isinstance(exception, OperandError)

    exception = calculation("&13/3")
    assert isinstance(exception, OperatorError)

    exception = calculation("15*10=150")
    assert isinstance(exception, UnidentifiedInputError)

    exception = calculation("0^0")
    assert isinstance(exception, OperatorError)


def test_gibberish():
    exception = calculation("dscad{}`דג/")
    assert isinstance(exception, UnidentifiedInputError)


def test_empty_expression():
    exception = calculation("")
    assert isinstance(exception, EmptyExpressionError)


def test_white_spaces():
    exception = calculation("       ")
    assert isinstance(exception, EmptyExpressionError)
