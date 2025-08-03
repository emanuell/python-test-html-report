import pytest
from src.calculator import Calculator, validate_email, fibonacci, process_list


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        result = self.calc.add(3, 5)
        assert result == 8
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-3, -5)
        assert result == -8
    
    def test_subtract_positive_numbers(self):
        result = self.calc.subtract(10, 3)
        assert result == 7
    
    def test_multiply_numbers(self):
        result = self.calc.multiply(4, 5)
        assert result == 20
    
    def test_divide_numbers(self):
        result = self.calc.divide(10, 2)
        assert result == 5.0
    
    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)


class TestEmailValidation:
    def test_valid_email(self):
        assert validate_email("test@example.com") is True
    
    def test_invalid_email_no_at(self):
        assert validate_email("testexample.com") is False
    
    def test_invalid_email_empty(self):
        assert validate_email("") is False
    
    def test_invalid_email_none(self):
        assert validate_email(None) is False
    
    def test_invalid_email_multiple_at(self):
        assert validate_email("test@@example.com") is False
    
    def test_invalid_email_no_domain(self):
        assert validate_email("test@") is False
    
    def test_invalid_email_no_username(self):
        assert validate_email("@example.com") is False


class TestFibonacci:
    def test_fibonacci_zero(self):
        assert fibonacci(0) == 0
    
    def test_fibonacci_one(self):
        assert fibonacci(1) == 1
    
    def test_fibonacci_positive(self):
        assert fibonacci(5) == 5
        assert fibonacci(8) == 21
    
    def test_fibonacci_negative_raises_error(self):
        with pytest.raises(ValueError, match="Input must be non-negative"):
            fibonacci(-1)


class TestProcessList:
    def test_process_empty_list(self):
        result = process_list([])
        assert result == []
    
    def test_process_string_list(self):
        result = process_list(["hello", "world"])
        assert result == ["HELLO", "WORLD"]
    
    def test_process_mixed_list(self):
        result = process_list(["hello", 123, "world", 45.6])
        assert result == ["HELLO", 123, "WORLD", 45.6]
    
    def test_process_none_input(self):
        result = process_list(None)
        assert result == []


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_calculator_add_parametrized(a, b, expected):
    calc = Calculator()
    result = calc.add(a, b)
    assert result == expected


def test_fibonacci_large_number():
    result = fibonacci(10)
    assert result == 55