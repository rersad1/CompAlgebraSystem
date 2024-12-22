from classes import *
from operations.rational_operations import RationalOperations
from operations.integer_operations import IntegerOperations
from operations.natural_operations import NaturalOperations

class PolynomialOperations:
    # P-1 Разработчик:Раутио.И
    @staticmethod
    def ADD_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Сложение двух многочленов.
        """
        result = Polynomial()

        # Копируем первый многочлен в результат
        current1 = poly1.head
        while current1:
            result.add_term(current1.degree, current1.coefficient)
            current1 = current1.next

        # Добавляем члены второго многочлена
        current2 = poly2.head
        while current2:
            found = False
            current_result = result.head
            
            # Ищем член с такой же степенью в результате
            while current_result:
                if int(current_result.degree) == int(current2.degree):
                    # Складываем коэффициенты
                    new_coefficient = RationalOperations.ADD_QQ_Q(current_result.coefficient, current2.coefficient)
                    # Обновляем коэффициент в результате
                    current_result.coefficient = new_coefficient
                    found = True
                    break
                current_result = current_result.next
                
            # Если не нашли член с такой степенью - добавляем новый
            if not found:
                result.add_term(current2.degree, current2.coefficient)
                
            current2 = current2.next

        return result

    # P-2 Разработчик:Потоцкий.С
    @staticmethod
    def SUB_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Вычитание двух многочленов через прямое вычитание коэффициентов.
        """
        result = Polynomial()

        # Копируем первый многочлен в результат
        current1 = poly1.head
        while current1:
            result.add_term(current1.degree, current1.coefficient)
            current1 = current1.next

        # Вычитаем члены второго многочлена
        current2 = poly2.head
        while current2:
            found = False
            current_result = result.head
            
            # Ищем член с такой же степенью в результате
            while current_result:
                if int(current_result.degree) == int(current2.degree):
                    # Вычитаем коэффициенты используя SUB_QQ_Q
                    new_coefficient = RationalOperations.SUB_QQ_Q(current_result.coefficient, current2.coefficient)
                    # Обновляем коэффициент в результате
                    current_result.coefficient = new_coefficient
                    found = True
                    break
                current_result = current_result.next
                
            # Если не нашли член с такой степенью - добавляем новый с противоположным знаком
            if not found:
                neg_coef = Rational(
                    IntegerOperations.MUL_ZM_Z(current2.coefficient.numerator),
                    current2.coefficient.denominator
                )
                result.add_term(current2.degree, neg_coef)
                
            current2 = current2.next

        return result

    # P-3 Разработчик:Березовский.М
    @staticmethod
    def MUL_PQ_P(poly: Polynomial, q: Rational) -> Polynomial:
        """
        Умножение многочлена на рациональное число.

        :param poly: Многочлен, который нужно умножить.
        :param q: Рациональное число, на которое нужно умножить многочлен.
        :return: Новый многочлен, результат умножения.
        """
        result = Polynomial()
        current = poly.head
        # Проходим по всем одночленам в многочлене
        while current:
            print(type(current.coefficient))
            print(current.coefficient, "КОЭФФИЦИЕНТ")
            print(current.coefficient.numerator, current.coefficient.denominator)
            # Умножаем коэффициент каждого одночлена на рациональное число
            print("В ЦИКЛЕ")
            print((current.coefficient.numerator, current.coefficient.denominator))
            new_coeff = Rational(current.coefficient.numerator, current.coefficient.denominator)
            print(new_coeff, "НОВЫЙ КОЭФФИЦИЕНТ")
            multiplied_coeff = RationalOperations.MUL_QQ_Q(new_coeff, q)

            # Добавляем результат умножения в новый многочлен
            result.add_term(current.degree, multiplied_coeff)
            # Переходим к следующему одночлену
            current = current.next

        return result

    # P-4 Разработчик: Тимошук.Е
    @staticmethod
    def MUL_Pxk_P(poly: Polynomial, k: Natural) -> Polynomial: # проверено
        """
        Умножение многочлена на x^k.

        :param poly: Многочлен, который нужно умножить.
        :param k: Натуральное число или 0, степень, на которую нужно умножить.
        :return: Новый многочлен, результат умножения.
        """
        result = Polynomial()

        current = poly.head

        # Проходим по всем одночленам в многочлене
        while current:
            # Увеличиваем степень на k
            new_degree = Natural(str(int(current.degree) + int(k)))

            # Добавляем одночлен с новой степенью в новый многочлен
            result.add_term(new_degree, current.coefficient)

            # Переходим к следующему одночлену
            current = current.next

        return result

    # P-5 Разработчик:Потапов.Р
    @staticmethod
    def LED_P_Q(poly: Polynomial) -> Rational: #проверено
        """
        Возвращает старший коэффициент многочлена.

        :param poly: Многочлен, для которого необходимо найти старший коэффициент.
        :return: Старший коэффициент многочлена.
        """
        current = poly.head
        max_degree = None
        leading_coefficient = None

        # Перебираем все одночлены многочлена
        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
                leading_coefficient = current.coefficient
            current = current.next

        return leading_coefficient

    # P-6 Разработчик:Потоцкий.С
    @staticmethod
    def DEG_P_N(poly: Polynomial) -> Natural: # проверено
        """
        Возвращает степень многочлена.

        :param poly: Многочлен, для которого необходимо найти степень.
        :return: Степень многочлена (Natural).
        """
        current = poly.head
        max_degree = None

        # Перебираем все одночлены многочлена
        while current:
            if max_degree is None or int(current.degree) > int(max_degree):
                max_degree = current.degree
            current = current.next

        return max_degree

    # P-7 Разработчик:Потапов.Р
    @staticmethod
    def FAC_P_Q(poly: Polynomial) -> Polynomial: #???
        """
        Вынесение НОК знаменателей коэффициентов и НОД числителей из многочлена.

        :param poly: Многочлен, для которого необходимо выполнить вынесение.
        :return: Новый многочлен с вынесенным НОК и НОД.
        """
        # Инициализация переменных для НОД числителей и НОК знаменателей
        lcm_denominator = Natural("1")
        gcf_numerator = Rational(Integer("1"))

        current = poly.head

        while current:
            coeff = current.coefficient
            numerator = coeff.numerator
            denominator = coeff.denominator

            # Абсолютные значения числителей и знаменателей
            abs_numerator = IntegerOperations.ABS_Z_N(numerator)
            abs_denominator = IntegerOperations.ABS_Z_N(denominator)

            # Преобразуем числитель и знаменатель в натуральные числа
            abs_numerator_nat = IntegerOperations.TRANS_Z_N(abs_numerator)
            abs_denominator_nat = IntegerOperations.TRANS_Z_N(abs_denominator)

            # Находим НОД числителей
            gcf_numerator = Rational(Integer(str(int(NaturalOperations.GCF_NN_N(gcf_numerator.numerator, abs_numerator_nat)))),
                                     Natural("1"))

            # Находим НОК знаменателей
            lcm_denominator = NaturalOperations.LCM_NN_N(lcm_denominator, abs_denominator_nat)

            current = current.next

        # Создадим новый многочлен, в котором все коэффициенты будут изменены
        result_poly = Polynomial()
        current = poly.head

        while current:
            coeff = current.coefficient
            # Применим деление целых чисел для числителя и знаменателя
            new_numerator = IntegerOperations.DIV_ZZ_Z(coeff.numerator, gcf_numerator.numerator)
            new_denominator = IntegerOperations.DIV_ZZ_Z(coeff.denominator, lcm_denominator)

            # Преобразуем результат обратно в целое число для знаменателя
            new_numerator_int = IntegerOperations.TRANS_N_Z(new_numerator)
            new_denominator_int = IntegerOperations.TRANS_N_Z(new_denominator)

            # Преобразуем результаты в рациональные числа
            new_coeff = Rational(new_numerator_int, new_denominator_int)
            result_poly.add_term(current.degree, new_coeff)

            current = current.next

        return result_poly

    # P-8 Разработчик:Потапов.Р
    @staticmethod
    def MUL_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Умножение двух многочленов.

        :param poly1: Первый многочлен.
        :param poly2: Второй многочлен.
        :return: Новый многочлен, который является произведением poly1 и poly2.
        """
        result_poly = Polynomial()  # Новый многочлен для результата

        # Проходим по всем одночленам первого многочлена
        current1 = poly1.head
        while current1:
            # Проходим по всем одночленам второго многочлена
            current2 = poly2.head
            while current2:
                # Умножаем коэффициенты
                new_coeff = Rational(
                    Integer(str(int(current1.coefficient.numerator) * int(current2.coefficient.numerator))),
                    Natural(str(int(current1.coefficient.denominator) * int(current2.coefficient.denominator)))
                )

                # Степень нового одночлена
                new_degree = Natural(str(int(current1.degree) + int(current2.degree)))

                # Умножение на x^k (где k - новая степень)
                temp_poly = Polynomial()

                # Для каждого произведения, используем MUL_Pxk_P
                temp_poly = PolynomialOperations.MUL_Pxk_P(temp_poly, new_degree)

                # Умножаем коэффициент на рациональное число (если нужно)
                temp_poly = PolynomialOperations.MUL_PQ_P(temp_poly, new_coeff)

                # Добавляем результат в итоговый многочлен
                result_poly = PolynomialOperations.ADD_PP_P(result_poly, temp_poly)

                current2 = current2.next
            current1 = current1.next

        return result_poly

    # P-9 Разработчик:Раутио.И
    @staticmethod
    def DIV_PP_P(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
        """
        Деление многочлена на многочлен без остатка.
        """
        quotient = Polynomial()
        dividend_current = dividend.head
        divisor_current = divisor.head
        
        while dividend_current.next:
            dividend_current = dividend_current.next
        while divisor_current.next:
            divisor_current = divisor_current.next
            
        while int(dividend_current.degree) >= int(divisor_current.degree):
            quotient_coeff = RationalOperations.DIV_QQ_Q(dividend_current.coefficient, divisor_current.coefficient)
            degree_diff = NaturalOperations.SUB_NN_N(dividend_current.degree, divisor_current.degree)
            quotient.add_term(degree_diff, quotient_coeff)
            print(quotient, "ЧАСТНОЕ")
            # Получаем вычитаемое

            temp_poly = PolynomialOperations.MUL_Pxk_P(divisor, degree_diff)
            print(temp_poly, "ВРЕМЕННЫЙ ДЛЯ ВЫЧИТАНИЯ")
            temp_poly = PolynomialOperations.MUL_PQ_P(temp_poly, quotient_coeff)

            dividend = PolynomialOperations.SUB_PP_P(dividend, temp_poly)
            
            dividend_current = dividend.head
            while dividend_current.next:
                dividend_current = dividend_current.next

        return quotient

    # P-10 Разработчик:Раутио.И
    @staticmethod
    def MOD_PP_P(dividend: Polynomial, divisor: Polynomial) -> Polynomial:
        """
        Остаток от деления многочлена на многочлен при делении с остатком.

        :param dividend: Многочлен-делимое.
        :param divisor: Многочлен-делитель.
        :return: Остаток от деления.
        """
        # Шаг 1: Получаем частное и остаток от деления
        print("ПЕРЕД ОСТАТКОМ ОТ ДЕЛЕНИЯ")
        quotient, remainder = PolynomialOperations.DIV_PP_P(dividend, divisor)
        print(quotient, remainder)
        # Шаг 2: Проверка остатка: remainder должно быть остатком после деления
        product = PolynomialOperations.MUL_PP_P(quotient, divisor)
        print("ПОСЛЕ ПОЛУЧЕНИЯ ПРОДАКТА")
        remainder_check = PolynomialOperations.SUB_PP_P(dividend, product)

        # Если remainder_check равен нулевому многочлену, значит остаток корректен
        # Однако, на практике, можно просто вернуть найденный остаток:
        return remainder

    # P-11 Разработчик:Потоцкий.С
    @staticmethod
    def GCF_PP_P(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        """
        Находит наибольший общий делитель (НОД) двух многочленов.

        :param poly1: Первый многочлен.
        :param poly2: Второй многочлен.
        :return: НОД двух многочленов.
        """
        # Применяем алгоритм Евклида для многочленов
        coefficient = PolynomialOperations.DEG_P_N(poly2)
        print('УСПЕХ ПОЛУЧЕНИЯ КОЭФФИЦИЕНТА')
        string_answer = NaturalOperations.NZER_N_B(coefficient)
        print('УСПЕХ ПОЛУЧЕНИЯ СТРОКОВОГО ОТВЕТА')
        while string_answer == "да":
            print("УЖЕ В ЦКИЛЕ")
            # Находим остаток от деления poly1 на poly2
            remainder = PolynomialOperations.MOD_PP_P(poly1, poly2)
            print("ПОЛУЧИЛИ ОСТАТОК")
            print(remainder)
            # Обновляем poly1 и poly2 для следующего шага алгоритма
            poly1, poly2 = poly2, remainder

            coefficient = PolynomialOperations.DEG_P_N(poly2)
            string_answer = NaturalOperations.NZER_N_B(coefficient)

        return remainder  # НОД - это последний ненулевой остаток

    # P-12 Разработчик:Потоцкий.С
    @staticmethod
    def DER_P_P(poly: Polynomial) -> Polynomial:
        """
        Находит производную многочлена.

        :param poly: Многочлен.
        :return: Производная многочлена.
        """
        derivative = Polynomial()
        current = poly.head.next  # Начинаем с первого одночлена

        while current:
            degree = current.degree
            coefficient = current.coefficient

            # Если степень больше 0, вычисляем производную одночлена
            if int(degree) > 0:
                # Производная одночлена a * x^n равна a * n * x^(n-1)
                new_coefficient = Rational(
                    Integer(str(int(coefficient.numerator) * int(degree)))
                )
                new_degree = Natural(str(int(degree) - 1))
                derivative.add_term(new_degree, new_coefficient)

            current = current.next

        return derivative

    # P-13 Разработчик:Тимошук.Е
    @staticmethod
    def NMR_P_P(poly: Polynomial) -> Polynomial:
        """
        Преобразование многочлена: кратные корни в простые.

        :param poly: Многочлен.
        :return: Многочлен с простыми корнями.
        """
        # Вычисляем производную многочлена
        derivative = PolynomialOperations.DER_P_P(poly)

        # Находим НОД (наибольший общий делитель) между многочленом и его производной
        gcd_poly = PolynomialOperations.GCF_PP_P(poly, derivative)

        # Разделим исходный многочлен на НОД, чтобы избавиться от кратных корней
        result_poly = PolynomialOperations.DIV_PP_P(poly, gcd_poly)

        return result_poly


# poly1 = create_polynomial("100x^243 - 30000x + 6789")
# print(f"{poly1}")
# poly2 = create_polynomial("x^3 - x + 2")
# poly3 = create_polynomial("-2x^4 + 7")
#
# res = PolynomialOperations.ADD_PP_P(poly1, poly2)
# print(res)