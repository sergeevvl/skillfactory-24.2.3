import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_pass(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_fail(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_pass(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_division_fail(self):
        assert self.calc.division(self, 4, 2) == 3

    def test_subtraction_pass(self):
        assert self.calc.subtraction(self, 6, 3) == 3

    def test_subtraction_fail(self):
        assert self.calc.division(self, 7, 3) == 5

    def test_adding_pass(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_fail(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')


