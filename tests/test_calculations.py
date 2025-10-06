import pytest
from app.calculation import CalculationFactory

def test_factory_add_and_execute():
    calc = CalculationFactory.create(1, 2, "add")
    assert calc.execute() == 3

def test_factory_subtract_and_execute():
    calc = CalculationFactory.create(10, 3, "subtract")
    assert calc.execute() == 7

def test_factory_multiply_and_execute():
    calc = CalculationFactory.create(3, 5, "multiply")
    assert calc.execute() == 15

def test_factory_division_and_execute():
    calc = CalculationFactory.create(20, 4, "divide")
    assert calc.execute() == 5

def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create(1,2,"pow")
