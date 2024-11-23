import unittest
from classes import Polynomial, Rational, Natural, Integer
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations


class TestPolynomialOperations(unittest.TestCase):

    def setUp(self):
        # Для тестирования создадим несколько примеров многочленов
        self.poly1 = Polynomial()
        self.poly2 = Polynomial()
        self.poly3 = Polynomial()

        # Добавление одночленов в poly1: 3x^2 + 2x + 1
        self.poly1.add_term(Natural("2"), Rational(Integer("3")))  # 3x^2
        self.poly1.add_term(Natural("1"), Rational(Integer("2")))  # 2x
        self.poly1.add_term(Natural("0"), Rational(Integer("1")))  # 1

        # Добавление одночленов в poly2: 4x^2 + 3x + 2
        self.poly2.add_term(Natural("2"), Rational(Integer("4")))  # 4x^2
        self.poly2.add_term(Natural("1"), Rational(Integer("3")))  # 3x
        self.poly2.add_term(Natural("0"), Rational(Integer("2")))  # 2

        # poly3: 5x^3 + 3x^2 + x
        self.poly3.add_term(Natural("3"), Rational(Integer("5")))  # 5x^3
        self.poly3.add_term(Natural("2"), Rational(Integer("3")))  # 3x^2
        self.poly3.add_term(Natural("1"), Rational(Integer("1")))  # x

    def test_add_polynomials(self):
        # Проверка сложения двух многочленов
        result = PolynomialOperations.ADD_PP_P(self.poly1, self.poly2)

        # Проверим полученный многочлен: (3x^2 + 2x + 1) + (4x^2 + 3x + 2) = 7x^2 + 5x + 3
        expected = Polynomial()
        expected.add_term(Natural("2"), Rational(Integer("7")))  # 7x^2
        expected.add_term(Natural("1"), Rational(Integer("5")))  # 5x
        expected.add_term(Natural("0"), Rational(Integer("3")))  # 3

        self.assertEqual(result, expected)

    def test_sub_polynomials(self):
        # Проверка вычитания двух многочленов
        result = PolynomialOperations.SUB_PP_P(self.poly1, self.poly2)

        # Проверим полученный многочлен: (3x^2 + 2x + 1) - (4x^2 + 3x + 2) = -x^2 - x - 1
        expected = Polynomial()
        expected.add_term(Natural("2"), Rational(Integer("-1")))  # -x^2
        expected.add_term(Natural("1"), Rational(Integer("-1")))  # -x
        expected.add_term(Natural("0"), Rational(Integer("-1")))  # -1

        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_rational(self):
        # Проверка умножения многочлена на рациональное число
        q = Rational(Integer("2"), Natural("1"))  # 2
        result = PolynomialOperations.MUL_PQ_P(self.poly1, q)

        # Ожидаем результат: 6x^2 + 4x + 2
        expected = Polynomial()
        expected.add_term(Natural("2"), Rational(Integer("6")))  # 6x^2
        expected.add_term(Natural("1"), Rational(Integer("4")))  # 4x
        expected.add_term(Natural("0"), Rational(Integer("2")))  # 2

        self.assertEqual(result, expected)

    def test_multiply_polynomial_by_xk(self):
        # Проверка умножения многочлена на x^k
        k = Natural("2")  # x^2
        result = PolynomialOperations.MUL_Pxk_P(self.poly1, k)

        # Ожидаем результат: 3x^4 + 2x^3 + x^2
        expected = Polynomial()
        expected.add_term(Natural("4"), Rational(Integer("3")))  # 3x^4
        expected.add_term(Natural("3"), Rational(Integer("2")))  # 2x^3
        expected.add_term(Natural("2"), Rational(Integer("1")))  # x^2

        self.assertEqual(result, expected)

    def test_gcf_polynomials(self):
        # Проверка нахождения НОД двух многочленов
        result = PolynomialOperations.GCF_PP_P(self.poly1, self.poly2)

        # Ожидаем результат: x^2 + x + 1 (наибольший общий делитель)
        expected = Polynomial()
        expected.add_term(Natural("2"), Rational(Integer("1")))  # x^2
        expected.add_term(Natural("1"), Rational(Integer("1")))  # x
        expected.add_term(Natural("0"), Rational(Integer("1")))  # 1

        self.assertEqual(result, expected)

    def test_derivative_polynomial(self):
        # Проверка нахождения производной многочлена
        result = PolynomialOperations.DER_P_P(self.poly1)

        # Ожидаем результат: 6x + 2
        expected = Polynomial()
        expected.add_term(Natural("1"), Rational(Integer("6")))  # 6x
        expected.add_term(Natural("0"), Rational(Integer("2")))  # 2

        self.assertEqual(result, expected)

    def test_divide_polynomials(self):
        # Проверка деления многочленов
        dividend = Polynomial()
        divisor = Polynomial()

        dividend.add_term(Natural("3"), Rational(Integer("5")))  # 5x^3
        dividend.add_term(Natural("2"), Rational(Integer("3")))  # 3x^2
        dividend.add_term(Natural("1"), Rational(Integer("1")))  # x

        divisor.add_term(Natural("2"), Rational(Integer("1")))  # x^2
        divisor.add_term(Natural("1"), Rational(Integer("2")))  # 2x
        divisor.add_term(Natural("0"), Rational(Integer("1")))  # 1

        quotient, remainder = PolynomialOperations.DIV_PP_P(dividend, divisor)

        # Ожидаем частное: 5x + 7, остаток: 0
        expected_quotient = Polynomial()
        expected_quotient.add_term(Natural("1"), Rational(Integer("5")))  # 5x
        expected_quotient.add_term(Natural("0"), Rational(Integer("7")))  # 7

        expected_remainder = Polynomial()  # Остаток 0

        self.assertEqual(quotient, expected_quotient)
        self.assertEqual(remainder, expected_remainder)



if __name__ == '__main__':
    unittest.main()