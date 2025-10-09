import pytest
from app.calculation.calculation import Calculation, CalculationFactory
from app.operation import operations

def test_add():
    calc = Calculation(1, 2, operations.add)
    assert calc.perform() == 3
    assert calc.execute() == 3

def test_repr():
    calc = Calculation(1, 2, operations.add)
    assert "Calculation" in repr(calc)

def test_divide_by_zero():
    calc = Calculation(1, 0, operations.divide)
    with pytest.raises(ZeroDivisionError):
        calc.perform()

def test_factory_good_ops():
    c = CalculationFactory.create(3, 4, "add")
    assert isinstance(c, Calculation)
    c = CalculationFactory.create(3, 4, operations.subtract)
    assert isinstance(c, Calculation)

def test_factory_invalid_op_str():
    with pytest.raises(ValueError):
        CalculationFactory.create(1, 2, "not_a_real_op")  # This covers line 25

def test_factory_invalid_op_type():
    with pytest.raises(ValueError):
        CalculationFactory.create(1, 2, None)  # This covers line 26
