import pytest
from ConstantsAndExceptions.exceptions import *
from Output.calculator import calculation


def test_simple_errors():
    with pytest.raises(OperandError):
        calculation()

    with pytest.raises(OperatorError):
        calculation()

    with pytest.raises(BracketsError):
        calculation()

    with pytest.raises(UnidentifiedInputError):
        calculation()

    with pytest.raises(OperatorError):
        calculation()
