import unittest
from classes import Rational, Integer, Natural
from operations.natural_operations import NaturalOperations
from operations.integer_operations import IntegerOperations
from operations.rational_operations import RationalOperations


class TestRationalOperations(unittest.TestCase):

    def test_RED_Q_Q(self):
        # Тест для сокращения дроби
        fraction = Rational(Integer("12"), Natural("16"))
        reduced_fraction = RationalOperations.RED_Q_Q(fraction)

        # Ожидаемая результат (сокращение 12/16 => 3/4)
        expected = Rational(Integer("3"), Natural("4"))

        self.assertEqual(reduced_fraction.numerator, expected.numerator)
        self.assertEqual(reduced_fraction.denominator, expected.denominator)

    def test_INT_Q_B(self):
        # Тест для проверки, является ли дробь целым числом
        fraction1 = Rational(Integer("6"), Natural("2"))
        fraction2 = Rational(Integer("7"), Natural("3"))

        self.assertEqual(RationalOperations.INT_Q_B(fraction1), "да")
        self.assertEqual(RationalOperations.INT_Q_B(fraction2), "нет")

    def test_TRANS_Z_Q(self):
        # Тест для преобразования целого числа в рациональное число
        integer = Integer("5")
        fraction = RationalOperations.TRANS_Z_Q(integer)

        # Ожидаемый результат: 5/1
        expected = Rational(Integer("5"), Natural("1"))

        self.assertEqual(fraction.numerator, expected.numerator)
        self.assertEqual(fraction.denominator, expected.denominator)

    def test_TRANS_Q_Z(self):
        # Тест для преобразования рационального числа в целое, если знаменатель равен 1
        rational = Rational(Integer("7"), Natural("1"))
        integer = RationalOperations.TRANS_Q_Z(rational)

        # Ожидаемый результат: 7
        expected = Integer("7")

        self.assertEqual(integer, expected)

        # Тест с исключением для дроби, которая не является целым числом
        rational2 = Rational(Integer("7"), Natural("3"))

        with self.assertRaises(ValueError):
            RationalOperations.TRANS_Q_Z(rational2)

    def test_ADD_QQ_Q(self):
        # Тест для сложения дробей
        fraction1 = Rational(Integer("1"), Natural("2"))
        fraction2 = Rational(Integer("1"), Natural("3"))

        result = RationalOperations.ADD_QQ_Q(fraction1, fraction2)

        # Ожидаемая сумма: 1/2 + 1/3 = (3 + 2) / 6 = 5/6
        expected = Rational(Integer("5"), Natural("6"))

        self.assertEqual(result.numerator, expected.numerator)
        self.assertEqual(result.denominator, expected.denominator)

    def test_SUB_QQ_Q(self):
        # Тест для вычитания дробей
        fraction1 = Rational(Integer("3"), Natural("4"))
        fraction2 = Rational(Integer("1"), Natural("4"))

        result = RationalOperations.SUB_QQ_Q(fraction1, fraction2)

        # Ожидаемый результат: 3/4 - 1/4 = 2/4 = 1/2
        expected = Rational(Integer("1"), Natural("2"))

        self.assertEqual(result.numerator, expected.numerator)
        self.assertEqual(result.denominator, expected.denominator)

    def test_MUL_QQ_Q(self):
        # Тест для умножения дробей
        fraction1 = Rational(Integer("3"), Natural("5"))
        fraction2 = Rational(Integer("2"), Natural("7"))

        result = RationalOperations.MUL_QQ_Q(fraction1, fraction2)

        # Ожидаемый результат: (3/5) * (2/7) = 6/35
        expected = Rational(Integer("6"), Natural("35"))

        self.assertEqual(result.numerator, expected.numerator)
        self.assertEqual(result.denominator, expected.denominator)

        def test_DIV_QQ_Q(self):
            # Тест для деления дробей
            fraction1 = Rational(Integer("3"), Natural("4"))
            fraction2 = Rational(Integer("2"), Natural("5"))

            result = RationalOperations.DIV_QQ_Q(fraction1, fraction2)

            # Ожидаемый результат: (3/4) / (2/5) = (3/4) * (5/2) = 15/8
            expected = Rational(Integer("15"), Natural("8"))

            self.assertEqual(result.numerator, expected.numerator)
            self.assertEqual(result.denominator, expected.denominator)

            # Тест с делением на ноль
            fraction3 = Rational(Integer("1"), Natural("0"))
            with self.assertRaises(ValueError):
                RationalOperations.DIV_QQ_Q(fraction1, fraction3)

if __name__ == "__main__":
    unittest.main()