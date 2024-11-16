from classes import *
from operations.natural_operations import NaturalOperations
class IntegerOperations:

    @staticmethod
    def ABS_Z_N(num: Integer) -> Natural:
        """
        Возвращает абсолютное значение целого числа как натуральное.
        """
        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строку из массива цифр.
        return Natural(digits_str)  # Создаем натуральное число.

    @staticmethod
    def POZ_Z_D(num: Integer) -> int:
        """
        Определяет знак числа:
        2 - положительное, 1 - отрицательное, 0 - равно нулю.
        """
        if len(num.get_digits()) == 1 and num.get_digits()[0] == 0:
            return 0  # Число равно нулю.
        return 1 if num.get_sign() else 2  # 1 - отрицательное, 2 - положительное.

    @staticmethod
    def MUL_ZM_Z(num: Integer) -> Integer:
        """
        Умножение целого числа на (-1).
        """
        # Создаем новое число с противоположным знаком.
        new_sign = not num.get_sign()  # Инвертируем знак.
        digits_str = ''.join(map(str, num.get_digits()))
        new_number = ('-' if new_sign else '') + digits_str
        return Integer(new_number)

    @staticmethod
    def TRANS_N_Z(num: Natural) -> Integer:
        """
        Преобразует натуральное число в целое.
        """
        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строку из цифр.
        return Integer(digits_str)  # Создаем положительное целое число.

    @staticmethod
    def TRANS_Z_N(num: Integer) -> Natural:
        """
        Преобразует целое число в натуральное.
        """
        if num.get_sign():  # Если знак отрицательный.
            raise ValueError("Отрицательное число нельзя преобразовать в натуральное.")
        digits_str = ''.join(map(str, num.get_digits()))  # Получаем строку из цифр.
        return Natural(digits_str)  # Создаем натуральное число.

    @staticmethod
    def ADD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Сложение двух целых чисел.
        """
        # Определяем знаки чисел.
        poz1 = IntegerOperations.POZ_Z_D(num1)  # Знак первого числа.
        poz2 = IntegerOperations.POZ_Z_D(num2)  # Знак второго числа.

        # Если одно из чисел равно 0, возвращаем другое.
        if poz1 == 0:
            return num2
        if poz2 == 0:
            return num1

        # Получаем модули чисел.
        abs_num1 = IntegerOperations.ABS_Z_N(num1)
        abs_num2 = IntegerOperations.ABS_Z_N(num2)

        if poz1 == poz2:  # Оба числа одного знака.
            # Складываем модули.
            sum_abs = NaturalOperations.ADD_NN_N(abs_num1, abs_num2)
            # Результат имеет общий знак.
            result_sign = num1.get_sign()
        else:  # Числа с разными знаками.
            # Определяем большее и меньшее число по модулю.
            comparison = NaturalOperations.COM_NN_D(abs_num1, abs_num2)
            if comparison == 2:  # abs_num1 > abs_num2
                difference = NaturalOperations.SUB_NN_N(abs_num1, abs_num2)
                result_sign = num1.get_sign()
            else:  # abs_num1 <= abs_num2
                difference = NaturalOperations.SUB_NN_N(abs_num2, abs_num1)
                result_sign = num2.get_sign()

            # Если результат равен 0, знак всегда положительный.
            if len(difference.get_digits()) == 1 and difference.get_digits()[0] == 0:
                result_sign = False

            sum_abs = difference

        # Создаем строку для результата.
        result_digits = ''.join(map(str, sum_abs.get_digits()))
        result_number = ('-' if result_sign else '') + result_digits
        return Integer(result_number)

    @staticmethod
    def SUB_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Вычитание двух целых чисел.
        :param num1: Уменьшаемое (целое число).
        :param num2: Вычитаемое (целое число).
        :return: Разность num1 и num2 (целое число).
        """
        # Определяем знак каждого числа
        poz_num1 = IntegerOperations.POZ_Z_D(num1)  # Знак num1
        poz_num2 = IntegerOperations.POZ_Z_D(num2)  # Знак num2

        # Преобразуем целые числа в натуральные (абсолютные значения)
        abs_num1 = IntegerOperations.ABS_Z_N(num1)  # Абсолютное значение num1
        abs_num2 = IntegerOperations.ABS_Z_N(num2)  # Абсолютное значение num2

        # Если числа имеют разные знаки, складываем их абсолютные значения
        if poz_num1 != poz_num2:
            # Складываем натуральные числа через ADD_NN_N
            result_abs = NaturalOperations.ADD_NN_N(abs_num1, abs_num2)

            # Если первое число отрицательное, меняем знак результата
            if poz_num1 == 1:
                result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
            else:
                result = Integer(str(result_abs))
        else:
            # Числа имеют одинаковый знак
            comparison = NaturalOperations.COM_NN_D(abs_num1, abs_num2)

            if comparison == 2:  # abs_num1 >= abs_num2
                # Вычитаем abs_num2 из abs_num1
                result_abs = NaturalOperations.SUB_NN_N(abs_num1, abs_num2)

                # Если числа отрицательные, меняем знак результата
                if poz_num1 == 1:
                    result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
                else:
                    result = Integer(str(result_abs))
            else:  # abs_num1 < abs_num2
                # Вычитаем abs_num1 из abs_num2
                result_abs = NaturalOperations.SUB_NN_N(abs_num2, abs_num1)

                # Если числа положительные, результат становится отрицательным
                if poz_num1 == 0:
                    result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
                else:
                    result = Integer(str(result_abs))

        return result

    @staticmethod
    def MUL_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Умножение двух целых чисел.
        :param num1: Первое целое число.
        :param num2: Второе целое число.
        :return: Результат умножения num1 и num2.
        """
        # Определяем знак каждого числа
        poz_num1 = IntegerOperations.POZ_Z_D(num1)  # Знак первого числа
        poz_num2 = IntegerOperations.POZ_Z_D(num2)  # Знак второго числа

        # Преобразуем оба числа в натуральные (абсолютные значения)
        abs_num1 = IntegerOperations.ABS_Z_N(num1)  # Абсолютное значение первого числа
        abs_num2 = IntegerOperations.ABS_Z_N(num2)  # Абсолютное значение второго числа

        # Умножаем натуральные числа через MUL_NN_N
        result_abs = NaturalOperations.MUL_NN_N(abs_num1, abs_num2)

        # Определяем знак результата
        # Числа имеют разные знаки, если один знак отрицательный
        if (poz_num1 == 1 and poz_num2 == 0) or (poz_num1 == 0 and poz_num2 == 1):
            # Результат отрицательный, меняем знак через MUL_ZM_Z
            result = IntegerOperations.MUL_ZM_Z(Integer(str(result_abs)))
        else:
            # Результат положительный
            result = Integer(str(result_abs))

        return result

    @staticmethod
    def DIV_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Деление одного целого числа на другое (делитель отличен от нуля).
        :param num1: Делимое - целое число.
        :param num2: Делитель - целое число.
        :return: Частное в виде целого числа.
        """
        # Проверяем делитель на ноль
        if IntegerOperations.POZ_Z_D(num2) == 0:
            raise ZeroDivisionError("Делитель не может быть равен нулю.")

        # Получаем абсолютные значения чисел
        abs_num1 = IntegerOperations.ABS_Z_N(num1)  # Абсолютное значение делимого
        abs_num2 = IntegerOperations.ABS_Z_N(num2)  # Абсолютное значение делителя

        # Выполняем деление абсолютных значений как натуральных чисел
        quotient_abs = NaturalOperations.DIV_NN_N(abs_num1, abs_num2)

        # Определяем знак результата
        poz_num1 = IntegerOperations.POZ_Z_D(num1)  # Знак делимого
        poz_num2 = IntegerOperations.POZ_Z_D(num2)  # Знак делителя

        if (poz_num1 == 1 and poz_num2 == 0) or (poz_num1 == 0 and poz_num2 == 1):
            # Результат отрицательный, добавляем знак минус
            quotient = IntegerOperations.MUL_ZM_Z(Integer(str(quotient_abs)))
        else:
            # Результат положительный
            quotient = Integer(str(quotient_abs))

        return quotient

    @staticmethod
    def MOD_ZZ_Z(num1: Integer, num2: Integer) -> Integer:
        """
        Вычисление остатка от деления целого на целое (делитель не равен нулю).
        :param num1: Делимое - целое число.
        :param num2: Делитель - целое число.
        :return: Остаток от деления в виде целого числа.
        """
        # Проверяем делитель на ноль
        if IntegerOperations.POZ_Z_D(num2) == 0:
            raise ZeroDivisionError("Делитель не может быть равен нулю.")

        # Вычисляем частное с помощью DIV_ZZ_Z
        quotient = IntegerOperations.DIV_ZZ_Z(num1, num2)

        # Умножаем частное на делитель (получаем ближайшее кратное)
        product = IntegerOperations.MUL_ZZ_Z(quotient, num2)

        # Вычитаем полученное кратное из делимого
        remainder = IntegerOperations.SUB_ZZ_Z(num1, product)

        # Знак остатка зависит от знака делимого и делителя
        if IntegerOperations.POZ_Z_D(num2) == 1:  # Делитель отрицательный
            remainder = IntegerOperations.MUL_ZM_Z(remainder)  # Меняем знак

        return remainder





