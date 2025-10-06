import pytest
from app.operation import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3), (2.5,0.5,3.0), (-1,1,0)
])
def test_add(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5,3,2), (0,1,-1), (2.5,0.5,2.0)
])
def test_subtract(a,b,expected):
    assert subtract(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2,3,6), (0,5,0), (0.5,2,1.0)
])
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected

def test_divide_ok():
    assert divide(6,3) == 2
    assert divide(5,2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)
