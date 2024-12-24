import re

class Integer:
    """
    Класс для работы с целыми числами, представленными в виде строки.
    Хранит число как массив цифр и его знак.
    """

    def __init__(self, number: str):
        """
        Инициализация объекта целого числа.

        :param number: Строка, представляющая целое число.
        """
        if not isinstance(number, str) or not number.lstrip('-').isdigit():
            raise ValueError("Некорректный формат: требуется строка, представляющая целое число.")

        self.is_negative = number.startswith('-')
        self.digits = [int(d) for d in number.lstrip('-')]

    def __str__(self):
        """
        Возвращает строковое представление числа.
        """
        sign = '-' if self.is_negative else ''
        return sign + ''.join(map(str, self.digits))

    def __int__(self):
        """
        Возвращает число в виде целого типа Python.
        """
        return int(str(self))

    def get_digits(self):
        """Возвращает массив цифр числа."""
        return self.digits

    def get_sign(self):
        """Возвращает знак числа (True для отрицательных)."""
        return self.is_negative

    def __len__(self):
        """Возвращает количество цифр в числе."""
        return len(self.digits)

    def __eq__(self, other):
        if isinstance(other, Integer):
            return str(self) == str(other)
        return False
    

class Natural:
    """
    Класс для работы с натуральными числами и нулем.
    """

    def __init__(self, number: str):
        """
        Инициализация натурального числа.

        :param number: Строка, представляющая натуральное число.
        """
        if not isinstance(number, str) or not number.isdigit() or int(number) < 0:
            raise ValueError("Некорректный формат: требуется строка, представляющая натуральное число или ноль.")

        self.digits = [int(d) for d in str(int(number))]

    def __str__(self):
        """
        Возвращает строковое представление числа.
        """
        return ''.join(map(str, self.digits))

    def __int__(self):
        """
        Возвращает число в виде целого типа Python.
        """
        return int(str(self))

    def get_digits(self):
        """Возвращает массив цифр числа."""
        return self.digits

    def __len__(self):
        """Возвращает количество цифр в числе."""
        return len(self.digits)

    def __eq__(self, other):
        if isinstance(other, Natural):
            return str(self) == str(other)
        return False
    
class Rational:
    """
    Класс для работы с рациональными числами.
    Хранит числитель как Integer и знаменатель как Natural.
    """

    def __init__(self, numerator: Integer, denominator: Natural = Natural("1")):
        """
        Инициализация рационального числа.

        :param numerator: Числитель (Integer).
        :param denominator: Знаменатель (Natural), по умолчанию равен 1.
        """
        if int(denominator) == 0:
            raise ValueError("Знаменатель не может быть нулём.")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Возвращает строковое представление рационального числа.
        """
        return f"{self.numerator}/{self.denominator}" if int(self.denominator) != 1 else str(self.numerator)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False
    
class PolynomialNode:
    """
    Узел двусвязного списка, представляющий одночлен многочлена.
    """

    def __init__(self, degree: Natural = Natural("0"), coefficient: Rational = Rational(Integer("0"))):
        """
        Инициализация узла.

        :param degree: Степень одночлена (Natural).
        :param coefficient: Коэффициент одночлена (Rational).
        """
        self.degree = degree
        self.coefficient = coefficient
        self.prev = None
        self.next = None


class Polynomial:
    """
    Класс для работы с многочленами, реализованными на основе двусвязного списка.
    """

    def __init__(self):
        """Инициализация пустого многочлена."""
        self.head = PolynomialNode()

    def __str__(self):
        """
        Возвращает строковое представление многочлена в порядке убывания степеней.
        """
        # Собираем все ненулевые члены в словарь, где ключ - степень
        terms = {}
        current = self.head
        while current:
            if int(current.coefficient.numerator) != 0:
                terms[int(current.degree)] = current
            current = current.next
        
        # Сортируем степени по убыванию
        sorted_degrees = sorted(terms.keys(), reverse=True)
        
        if not sorted_degrees:
            return "0"
            
        result = []
        for degree in sorted_degrees:
            coeff = int(terms[degree].coefficient.numerator)
            if coeff != 0:
                sign = " - " if coeff < 0 else (" + " if result else "")
                abs_coeff = abs(coeff)
                coeff_str = "" if abs_coeff == 1 and int(degree) > 0 else str(abs_coeff)
                
                if int(degree) > 1:
                    term = f"{coeff_str}x^{degree}"
                elif int(degree) == 1:
                    term = f"{coeff_str}x"
                else:
                    term = str(abs_coeff)
                    
                result.append(sign + term)
                
        return ''.join(result) if result else "0"

    def add_term(self, degree: Natural, coefficient: Rational):
        """
        Добавляет или обновляет одночлен в многочлене.

        :param degree: Степень одночлена.
        :param coefficient: Коэффициент одночлена.
        """
        if int(coefficient.numerator) == 0:
            return

        current = self.head
        while current:
            if current.degree == degree:
                current.coefficient = Rational(
                    Integer(str(int(current.coefficient.numerator) + int(coefficient.numerator))),
                    Natural(str(int(current.coefficient.denominator)))
                )
                return
            elif int(current.degree) > int(degree) and current.next:
                current = current.next
            else:
                new_node = PolynomialNode(degree, coefficient)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return

    def build_from_string(self, input_str: str):
        terms = re.split(r'(?=[+-])', input_str.replace(' ', '').replace('*', ''))
        for term in terms:
            if not term:  # Пропускаем пустые члены
                continue
            term = term.lstrip('+')  # Убираем "+" в начале

            if 'x' in term:
                if '^' in term:
                    coeff, _, degree = term.partition('x^')  # Разделяем коэффициент и степень
                else:
                    coeff, _, degree = term.partition('x')
                    degree = "1"  # Если степень не указана, это "x^1"

                if not coeff:  # Если коэффициент отсутствует, считаем "1"
                    coeff = "1"
                elif coeff == "-":  # Если коэффициент "-", заменяем на "-1"
                    coeff = "-1"
            else:
                coeff = term  # Для свободного члена
                degree = "0"

            # Отладочный вывод
            # print(f"Term: '{term}', Coefficient: '{coeff}', Degree: '{degree}'")

            # Проверка перед вызовом Integer
            if not coeff.isdigit() and not (coeff.startswith('-') and coeff[1:].isdigit()):
                raise ValueError(f"Некорректный коэффициент: '{coeff}'")

            self.add_term(Natural(degree), Rational(Integer(coeff)))
    
    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            return False
            
        # Преобразуем оба многочлена в строки для сравнения
        return str(self) == str(other)        

def create_polynomial(input_str: str) -> Polynomial:
    """
    Утилита для создания многочлена из строки.

    :param input_str: Строка, представляющая многочлен.
    :return: Экземпляр Polynomial.
    """
    poly = Polynomial()
    poly.build_from_string(input_str)
    return poly


# poly1 = create_polynomial("100x^243 - 30000x + 6789")
# print(f"{poly1}")
# poly2 = create_polynomial("x^3 - x + 2")
# poly3 = create_polynomial("-2x^4 + 7")
# print(f"Polynomial from '3x^2 + 4x - 5': {poly1}")
# print(f"Polynomial from 'x^3 - x + 2': {poly2}")
# print(f"Polynomial from '-2x^4 + 7': {poly3}")

# def test_polynomial():
#     print("=== Тестирование класса Polynomial ===")
#
#     try:
#         # Тест создания многочлена из строки
#         print("\nСоздание многочлена из строки: '3x^2 + 4x - 5'")
#         poly1 = create_polynomial("3x^2 + 4x - 5")
#         print(f"Многочлен 1: {poly1}")
#
#         # Тест добавления члена
#         print("\nДобавление члена 2x^3 в многочлен")
#         poly1.add_term(Natural("3"), Rational(Integer("2")))  # Добавляем 2x^3
#         print(f"После добавления: {poly1}")
#
#         # Тест создания второго многочлена
#         print("\nСоздание второго многочлена из строки: 'x^3 - x + 2'")
#         poly2 = create_polynomial("x^3 - x + 2")
#         print(f"Многочлен 2: {poly2}")
#
#         # Проверка строкового представления многочленов
#         print("\nСтроковое представление многочленов:")
#         print(f"Многочлен 1: {str(poly1)}")
#         print(f"Многочлен 2: {str(poly2)}")
#
#         poly3 = create_polynomial("6")
#         poly3.add_term(Natural("0"), Rational(Integer("4")))
#         print(poly3)
#
#     except Exception as e:
#         print(f"Ошибка при тестировании: {e}")
#
#
# if __name__ == "__main__":
#     test_polynomial()

