from classes import *
from operations.rational_operations import RationalOperations
from operations.integer_operations import IntegerOperations
from operations.natural_operations import NaturalOperations

class PolynomialOperations:
    @staticmethod
    def ADD_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        result = Polynomial()
        current1 = poly1.head
        while current1:
            result.add_term(current1.degree, current1.coefficient)
            current1 = current1.next

        current2 = poly2.head
        while current2:
            degree2 = current2.degree
            coefficient2 = current2.coefficient
            current1 = poly1.head
            while current1:
                if current1.degree == degree2:
                    new_coefficient = RationalOperations.ADD_QQ_Q(current1.coefficient, coefficient2)
                    result.add_term(degree2, new_coefficient)
                    break
                current1 = current1.next
            else:
                result.add_term(degree2, coefficient2)

            current2 = current2.next

        return result

    @staticmethod
    def SUB_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        result = Polynomial()
        current1 = poly1.head
        current2 = poly2.head

        while current1 or current2:
            if current1 and (not current2 or int(current1.degree) > int(current2.degree)):
                result.add_term(current1.degree, current1.coefficient)
                current1 = current1.next
            elif current2 and (not current1 or int(current2.degree) > int(current1.degree)):
                result.add_term(current2.degree, Rational(Integer("-" + str(current2.coefficient.numerator))))
                current2 = current2.next
            else:
                coeff_diff = Rational(Integer(str(int(current1.coefficient.numerator) - int(current2.coefficient.numerator))))
                if coeff_diff.numerator != 0:
                    result.add_term(current1.degree, coeff_diff)
                current1 = current1.next
                current2 = current2.next

        return result

    @staticmethod
    def MUL_PQ_P(poly: Polynomial, q: Rational) -> Polynomial:
        result = Polynomial()
        current = poly.head
        while current:
            multiplied_coeff = RationalOperations.MUL_QQ_Q(current.coefficient, q)
            result.add_term(current.degree, multiplied_coeff)
            current = current.next

        return result

    @staticmethod
    def MUL_Pxk_P(poly: Polynomial, k: Natural) -> Polynomial:
        result = Polynomial()
        current = poly.head
        while current:
            new_degree = Natural(str(int(current.degree) + int(k)))
            result.add_term(new_degree, current.coefficient)
            current = current.next

        return result

    @staticmethod
    def LED_P_Q(poly: Polynomial) -> Rational:
        current = poly.head
        max_degree = None
        leading_coefficient = None

        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
                leading_coefficient = current.coefficient
            current = current.next

        return leading_coefficient

    @staticmethod
    def DEG_P_N(poly: Polynomial) -> Natural:
        current = poly.head
        max_degree = None
        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
            current = current.next

        return max_degree

    @staticmethod
    def FAC_P_Q(poly: Polynomial) -> Polynomial:
        lcm_denominator = Natural("1")
        gcf_numerator = Rational(Integer("1"))
        current = poly.head

        while current:
            coeff = current.coefficient
            numerator = coeff.numerator
            denominator = coeff.denominator

            abs_numerator = IntegerOperations.ABS_Z_N(numerator)
            abs_denominator = IntegerOperations.ABS_Z_N(denominator)

            abs_numerator_nat = IntegerOperations.TRANS_Z_N(abs_numerator)
            abs_denominator_nat = IntegerOperations.TRANS_Z_N(abs_denominator)

            gcf_numerator = Rational(Integer(str(int(NaturalOperations.GCF_NN_N(gcf_numerator.numerator, abs_numerator_nat)))),
                                     Natural("1"))

            lcm_denominator = NaturalOperations.LCM_NN_N(lcm_denominator, abs_denominator_nat)
            current = current.next

        result_poly = Polynomial()
        current = poly.head

        while current:
            coeff = current.coefficient
            new_numerator = IntegerOperations.DIV_ZZ_Z(coeff.numerator, gcf_numerator.numerator)
            new_denominator = IntegerOperations.DIV_ZZ_Z(coeff.denominator, lcm_denominator)

            new_numerator_int = IntegerOperations.TRANS_N_Z(new_numerator)
            new_denominator_int = IntegerOperations.TRANS_N_Z(new_denominator)

            new_coeff = Rational(new_numerator_int, new_denominator_int)
            result_poly.add_term(current.degree, new_coeff)

            current = current.next

        return result_poly

    @staticmethod
    def MUL_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        result_poly = Polynomial()
        current1 = poly1.head
        while current1:
            current2 = poly2.head
            while current2:
                new_coeff = Rational(
                    Integer(str(int(current1.coefficient.numerator) * int(current2.coefficient.numerator))),
                    Natural(str(int(current1.coefficient.denominator) * int(current2.coefficient.denominator)))
                )
                new_degree = Natural(str(int(current1.degree) + int(current2.degree)))
                result_poly.add_term(new_degree, new_coeff)
                current2 = current2.next
            current1 = current1.next

        return result_poly

    @staticmethod
    def DIV_PP_P(dividend: Polynomial, divisor: Polynomial) -> (Polynomial, Polynomial):
        quotient = Polynomial()
        remainder = Polynomial()
        remainder.head = dividend.head

        while int(PolynomialOperations.DEG_P_N(remainder)) >= int(PolynomialOperations.DEG_P_N(divisor)):
            leading_term_remainder = remainder.head
            leading_term_divisor = divisor.head

            quotient_coeff = RationalOperations.DIV_QQ_Q(leading_term_remainder.coefficient, leading_term_divisor.coefficient)

            degree_diff = Natural(str(int(leading_term_remainder.degree) - int(leading_term_divisor.degree)))
            quotient.add_term(degree_diff, quotient_coeff)

            temp_poly = PolynomialOperations.MUL_Pxk_P(divisor, degree_diff)
            temp_poly = PolynomialOperations.MUL_PQ_P(temp_poly, quotient_coeff)
            remainder = PolynomialOperations.SUB_PP_P(remainder, temp_poly)

        return quotient, remainder

    @staticmethod
    def MOD_PP_P(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
        quotient, remainder = PolynomialOperations.DIV_PP_P(dividend, divisor)
        product = PolynomialOperations.MUL_PP_P(quotient, divisor)
        remainder_check = PolynomialOperations.SUB_PP_P(dividend, product)
        return remainder

    @staticmethod
    def GCF_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        while PolynomialOperations.DEG_P_N(poly2) > 0:
            remainder = PolynomialOperations.MOD_PP_P(poly1, poly2)
            poly1, poly2 = poly2, remainder

        return poly1

    @staticmethod
    def DER_P_P(poly: Polynomial) -> Polynomial:
        derivative = Polynomial()
        current = poly.head.next

        while current:
            degree = current.degree
            coefficient = current.coefficient
            if int(degree) > 0:
                new_coefficient = Rational(
                    Integer(str(int(coefficient.numerator) * int(degree)))
                )
                new_degree = Natural(str(int(degree) - 1))
                derivative.add_term(new_degree, new_coefficient)

            current = current.next

        return derivative

    @staticmethod
    def NMR_P_P(poly: Polynomial) -> Polynomial:
        derivative = PolynomialOperations.DER_P_P(poly)
        gcd_poly = PolynomialOperations.GCF_PP_P(poly, derivative)
        result_poly = PolynomialOperations.DIV_PP_P(poly, gcd_poly)

        return result_poly
