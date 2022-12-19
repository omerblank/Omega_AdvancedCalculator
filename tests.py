import pytest
from ConstantsAndExceptions.exceptions import *
from Output.calculator import calculation
from Input.input_calculations import calculate


# module for tests

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


def test_simple_expressions():
    # 1
    result = calculate("-0.2468#")
    assert result == -20

    # 2
    result = calculate("2%10")
    assert result == 2

    # 3
    result = calculate("17+3")
    assert result == 20

    # 4
    result = calculate("23&-23")
    assert result == -23

    # 5
    result = calculate("2*22")
    assert result == 44

    # 6
    result = calculate("10^2")
    assert result == 100

    # 7
    result = calculate("10@100")
    assert result == 55

    # 8
    result = calculate("37$36")
    assert result == 37

    # 9
    result = calculate("3!")
    assert result == 6

    # 10
    result = calculate("~99")
    assert result == -99

    # 11
    result = calculate("0.05*-100")
    assert result == -5

    # 12
    result = calculate("30/-30")
    assert result == -1

    # 13
    result = calculate("2*(8+2)")
    assert result == 20

    # 14
    result = calculate("20---80")
    assert result == -60

    # 15
    result = calculate("9.99111#")
    assert result == 30


def test_complicated_expressions():
    # 1
    result = calculate("---63  +    74##!/--~9^(2+3*(4--6))")
    assert result == -63

    # 2
    result = calculate("        (3 @ ----3!#*10)#---~(36/4)#+~-2")
    assert result == 20

    # 3
    result = calculate("(-~0.2468#/20)!#!#^9999*1000 @   100 0 #+9")
    assert result == 509.5

    # 4
    result = calculate("(1 *2*3*4*5*6)/6!#!#    ---~40---10*(1000/1000+0.0000#)")
    assert result == 56.66666666666667

    # 5
    result = calculate("(~(~--3*~--     -3+---~3/   3!)*-1+3000)&300")
    assert result == 300

    # 6
    result = calculate("((3/2* 2/2*2/2* 2)*3/9+0.7    3)#/11*~--100 ")
    assert result == -100

    # 7
    result = calculate("(5$-5    *~---------(2^3/8)  %2)!")
    assert result == 120

    # 8
    result = calculate("(-~3/~      -3----1.8)#/20  *9999+1!#!#!")
    assert result == 5000.5

    # 9
    result = calculate("    3+7*10+27&101   -----~3000  0#-~90$999")
    assert result == -896

    # 10
    result = calculate("500@1100--(     400$100)/200#   !+777-~12^0")
    assert result == 1776

    # 11
    result = calculate("1.234#+90 +900---1000*1--~0+--(  99+1)/1000")
    assert result == 0.1

    # 12
    result = calculate("-~2!!*~--1  0/1000+3333#+(~(2+3)@10   0)+------999")
    assert result == 1058.48

    # 13
    result = calculate("((4*4--4^2)%32+999999999 99999)/99999999 99999+5!")
    assert result == 130.0000000000009

    # 14
    result = calculate("20+-------~1000@1#!/3 309------9999+3$(4  44.4)")
    assert result == 10463.551254155334

    # 15
    result = calculate("16#+7----7--~-7+7*4------ 99.11#/200#!")
    assert result == 66

    # 16
    result = calculate("-9.8756234#+123124/10000+------(999#/1@334)")
    assert result == -31.526405970149252

    # 17
    result = calculate("(3*(4*(5*10)))#+1000-------~2 323+(99    /99*99@99)@99/2")
    assert result == 3378.5

    # 18
    result = calculate("233232323$1 /23323232    3+9%2+10%2!+3331#----~2+~ -3!")
    assert result == 16

    # 19
    result = calculate("((24*8)*0.001+81----~24 .8/81/1+--~2  4.81)&24")
    assert result == 24
