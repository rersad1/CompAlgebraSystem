from classes import *

class NaturalOperations:

    @staticmethod
    def COM_NN_D(num1: Natural, num2: Natural) -> int: #works
        """
        Сравнение двух натуральных чисел.
        Возвращает:
        - 2, если num1 > num2
        - 1, если num1 < num2
        - 0, если num1 == num2
        """
        # Сравниваем длины чисел
        if len(num1.digits) > len(num2.digits):
            return 2
        elif len(num1.digits) < len(num2.digits):
            return 1
        else:
            # Если длины равны, сравниваем цифры по порядку
            for i in range(len(num1.digits)):
                if num1.digits[i] > num2.digits[i]:
                    return 2
                elif num1.digits[i] < num2.digits[i]:
                    return 1
            return 0

    @staticmethod
    def NZER_N_B(num: Natural) -> str: #works
        """
        Проверка на ноль: если число не равно нулю, то «да», иначе «нет»
        """
        if len(num.digits) == 1 and num.digits[0] == 0:
            return "нет"
        return "да"

    @staticmethod
    def ADD_1N_N(num: Natural) -> Natural: #works
        """
        Добавление 1 к натуральному числу.
        """
        carry = 1
        result_digits = num.digits[::-1]  # переворачиваем, чтобы сложение было проще

        # Пытаемся добавить 1, начиная с младших разрядов
        for i in range(len(result_digits)):
            result_digits[i] += carry
            if result_digits[i] == 10:
                result_digits[i] = 0
                carry = 1
            else:
                carry = 0
                break

        if carry == 1:
            result_digits.append(1)

        result_digits.reverse()  # возвращаем порядок цифр в нормальное состояние
        return Natural(''.join(map(str, result_digits)))

    def ADD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Сложение двух натуральных чисел.
        """
        carry = 0
        result_digits = []

        len1, len2 = len(num1.digits), len(num2.digits)
        max_len = max(len1, len2)

        # Сложение по разрядам с учетом переноса
        for i in range(max_len):
            digit1 = num1.digits[len1 - i - 1] if i < len1 else 0
            digit2 = num2.digits[len2 - i - 1] if i < len2 else 0

            total = digit1 + digit2 + carry
            result_digits.append(total % 10)
            carry = total // 10

        if carry:
            result_digits.append(carry)

        result_digits.reverse()
        return Natural(''.join(map(str, result_digits)))

    @staticmethod
    def SUB_NN_N(num1: Natural, num2: Natural) -> Natural: #works
        """
        Вычитание из первого большего натурального числа второго меньшего или равного.
        Используется операция сравнения для вычитания столбиком.
        """
        # Сначала сравниваем два числа
        comparison = NaturalOperations.COM_NN_D(num1, num2)
        if comparison == 1:
            raise ValueError("Первое число должно быть больше или равно второму.")

        result_digits = []
        borrow = 0

        # Дополняем нулями числа до одинаковой длины
        if comparison == 1:
            num1.digits = [0] * (len(num2.digits) - len(num1.digits)) + num1.digits
        elif comparison == 2:
            num2.digits = [0] * (len(num1.digits) - len(num2.digits)) + num2.digits

        # Вычитаем числа столбиком
        for i in range(len(num1.digits) - 1, -1, -1):
            temp_diff = num1.digits[i] - num2.digits[i] - borrow
            if temp_diff < 0:
                temp_diff += 10
                borrow = 1
            else:
                borrow = 0
            result_digits.append(temp_diff)

        # Убираем ведущие нули
        while len(result_digits) > 1 and result_digits[-1] == 0:
            result_digits.pop()

        result_digits.reverse()
        return Natural(''.join(map(str, result_digits)))



    @staticmethod
    def MUL_ND_N(num: Natural, digit: int) -> Natural:
        """
        Умножение натурального числа на цифру (от 0 до 9).
        """
        if not (0 <= digit <= 9):
            raise ValueError("Цифра должна быть в пределах от 0 до 9.")

        result_digits = []
        carry = 0

        # Перемножаем каждый разряд числа на цифру
        for i in range(len(num.digits) - 1, -1, -1):
            temp_product = num.digits[i] * digit + carry
            result_digits.append(temp_product % 10)
            carry = temp_product // 10

        # Если есть перенос, добавляем его
        if carry:
            result_digits.append(carry)

        # Переворачиваем результат, чтобы вернуть правильный порядок цифр
        result_digits.reverse()
        return Natural(''.join(map(str, result_digits)))

    @staticmethod
    def MUL_Nk_N(num: Natural, k: int) -> Natural:
        """
        Умножение натурального числа на 10^k, где k — натуральное число.
        """
        if k < 0:
            raise ValueError("k должно быть натуральным числом (неотрицательным).")

        # Умножение на 10^k эквивалентно добавлению k нулей к числу
        result_digits = num.digits + [0] * k
        return Natural(''.join(map(str, result_digits)))

    @staticmethod
    def MUL_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Умножение двух натуральных чисел.
        Используется умножение на цифру и умножение на 10^k.
        """
        result = Natural("0")  # Начальное значение результата - ноль.

        for i in range(len(num2)):  # Перебираем цифры второго числа (num2).
            digit = num2.digits[len(num2) - i - 1]  # Цифра из num2.
            temp = NaturalOperations.MUL_ND_N(num1, digit)  # Умножаем num1 на цифру.
            temp = NaturalOperations.MUL_Nk_N(temp, i)  # Умножаем на 10^i (сдвигаем на разряд).
            result = NaturalOperations.ADD_NN_N(result, temp)  # Прибавляем результат к общему.

        return result

    @staticmethod
    def SUB_NDN_N(num1: Natural, num2: Natural, digit: int) -> Natural:
        """
        Вычитание из натурального числа num1 числа, полученного умножением num2 на digit.
        Предполагаем, что результат неотрицательный.
        """
        # Умножаем num2 на digit
        temp = NaturalOperations.MUL_ND_N(num2, digit)

        # Сравниваем num1 и temp для проверки, что вычитание возможно.
        if NaturalOperations.COM_NN_D(num1, temp) == 1:  # Если num1 < temp, то вычитание невозможно.
            raise ValueError("Результат вычитания будет отрицательным.")

        # Вычитаем temp из num1
        result = NaturalOperations.SUB_NN_N(num1, temp)
        return result

    @staticmethod
    def DIV_NN_Dk(num1: Natural, num2: Natural, k: int) -> int:
        """
        Вычисление первой цифры деления двух чисел,
        домноженной на 10^k, где k — это номер позиции цифры.
        """

        # Преобразуем числа в строковое представление для удобства работы
        larger_digits = ''.join(map(str, num1.digits))
        smaller_digits = ''.join(map(str, num2.digits))

        # Домножаем num2 на 10^k
        num2_modified = NaturalOperations.MUL_Nk_N(num2, k)
        modified_smaller_digits = ''.join(map(str, num2_modified.digits))

        # Выполняем деление
        quotient = int(larger_digits) // int(modified_smaller_digits)

        # Извлекаем первую цифру от деления
        first_digit = int(str(quotient)[0])

        return first_digit

    @staticmethod
    def DIV_NN_N(num1: Natural, num2: Natural) -> (Natural, Natural):
        """
        Неполное частное от деления первого натурального числа на второе с остатком.
        Предполагается, что делитель (num2) не равен нулю.
        """
        if NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Делитель не может быть нулём.")

        quotient = Natural("0")  # Изначально частное равно нулю.
        remainder = Natural(str(num1))  # Остаток изначально равен числу num1.



        # Пока остаток больше или равен делителю
        while NaturalOperations.COM_NN_D(remainder, num2) != 1:
            # Находим первую цифру частного с использованием DIV_NN_Dk
            first_digit = NaturalOperations.DIV_NN_Dk(remainder, num2, 0)
            # Добавляем эту цифру к частному
            quotient = NaturalOperations.ADD_NN_N(quotient, Natural(str(first_digit)))
            # Вычитаем из остатка num2, умноженное на первую цифру, с использованием SUB_NDN_N
            remainder = NaturalOperations.SUB_NDN_N(remainder, num2, first_digit)

        return quotient, remainder

    @staticmethod
    def MOD_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление остатка от деления первого натурального числа на второе.
        Предполагается, что делитель (num2) не равен нулю.
        """
        if int(num2) == 0:
            raise ValueError("Делитель не может быть нулём.")

        # Находим неполное частное от деления
        quotient, remainder = NaturalOperations.DIV_NN_N(num1, num2)

        # Остаток от деления — это исходное число минус частное, умноженное на делитель
        remainder = NaturalOperations.SUB_NDN_N(num1, num2, int(quotient))

        return remainder

    @staticmethod
    def GCF_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наибольшего общего делителя (НОД) двух натуральных чисел.
        Используется алгоритм Евклида.
        """
        # Проверяем, не равен ли одно из чисел нулю
        if NaturalOperations.NZER_N_B(num1) == "нет" or NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Число не может быть равно нулю.")

        while True:
            # Проверяем, не нужно ли менять местами числа перед расчетом остатка
            if NaturalOperations.COM_NN_D(num1, num2) < 0:
                num1, num2 = num2, num1

            # Получаем остаток от деления
            remainder = NaturalOperations.MOD_NN_N(num1, num2)

            # Если остаток равен нулю, то возвращаем второе число как НОД
            if NaturalOperations.COM_NN_D(remainder, Natural("0")) == 0:
                return num2

            # Если остаток не равен нулю, продолжаем с новым делителем
            num1, num2 = num2, remainder

    @staticmethod
    def LCM_NN_N(num1: Natural, num2: Natural) -> Natural:
        """
        Вычисление наименьшего общего кратного (НОК) двух натуральных чисел.
        Используется формула: LCM(a, b) = (a * b) / GCF(a, b)
        """
        if NaturalOperations.NZER_N_B(num1) == "нет" or NaturalOperations.NZER_N_B(num2) == "нет":
            raise ValueError("Число не может быть равно нулю.")

        # Находим НОД чисел
        gcf = NaturalOperations.GCF_NN_N(num1, num2)

        # Умножаем числа и делим на НОД для нахождения НОК
        product = NaturalOperations.MUL_NN_N(num1, num2)
        lcm = NaturalOperations.DIV_NN_N(product, gcf)

        return lcm


