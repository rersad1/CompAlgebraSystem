import unittest
from classes import *
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations


class TestPolynomialOperations(unittest.TestCase):

    def setUp(self):
        self.poly1 = create_polynomial("3x^2+2x+1")
        self.poly2 = create_polynomial("4x^2+3x+2")
        self.poly3 = create_polynomial("5x^3+3x^2+x")

    def test_add_polynomials(self):
        # Проверка сложения двух многочленов
        result = PolynomialOperations.ADD_PP_P(self.poly1, self.poly3)
        # Проверим полученный многочлен: (3x^2 + 2x + 1) + (4x^2 + 3x + 2) = 7x^2 + 5x + 3
        expected = create_polynomial("5x^3 + 6x^2 + 3x + 1")
        self.assertEqual(result, expected)

    def test_sub_polynomials(self):
        result = PolynomialOperations.SUB_PP_P(self.poly1, self.poly2)
        expected = create_polynomial("-x^2-x-1")
        print(expected)
        print(result)
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

        dividend.add_term(Natural("3"), Rational(Integer("4")))  # 5x^3
        dividend.add_term(Natural("1"), Rational(Integer("2")))  # 3x^2
        dividend.add_term(Natural("0"), Rational(Integer("-11")))  # x

        divisor.add_term(Natural("1"), Rational(Integer("1")))  # 2x
        divisor.add_term(Natural("0"), Rational(Integer("5")))  # 1

        quotient = PolynomialOperations.DIV_PP_P(dividend, divisor)

        # Ожидаем частное: 5x + 7, остаток: 0
        expected_quotient = Polynomial()
        expected_quotient.add_term(Natural("1"), Rational(Integer("5")))  # 5x
        expected_quotient.add_term(Natural("0"), Rational(Integer("7")))  # 7
        print(expected_quotient)

        self.assertEqual(quotient, expected_quotient)



if __name__ == '__main__':
    unittest.main()