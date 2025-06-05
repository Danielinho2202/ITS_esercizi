from  my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    return Calculator (10,5)

def test_addition(calculation):
    assert calculation.addition()== 13, 'sum wrong'

def test_subtraction(calculation):
    assert calculation.subtraction()== 5, 'sub wrong'

def test_multiplication(calculation):
    assert calculation.multiplication()== 50, 'mol wrong'

def test_division(calculation):
    assert calculation.division()== 2.00, 'div wrong'

