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
        Возвращает строковое представление многочлена.
        """
        terms = []
        current = self.head
        while current:
            coeff = int(current.coefficient.numerator)
            if coeff != 0:
                sign = " - " if coeff < 0 else (" + " if terms else "")
                abs_coeff = abs(coeff)
                term = f"{abs_coeff}x^{current.degree}" if int(current.degree) > 1 else \
                    (f"{abs_coeff}x" if int(current.degree) == 1 else str(abs_coeff))
                terms.append(sign + term)
            current = current.next
        return ''.join(terms) if terms else "0"

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
        """
        Создает многочлен из входной строки.

        :param input_str: Строка, представляющая многочлен.
        """
        terms = re.split(r'(?=[+-])', input_str.replace(' ', '').replace('*', ''))
        for term in terms:
            term = term.lstrip('+')
            if 'x' in term:
                coeff, _, degree = term.partition('x^')
                # Проверяем коэффициент на наличие пустой строки или знаков "+", "-"
                if coeff in ["", "+"]:  # Для случая "x^2" или "+x^2"
                    coeff = "1"
                elif coeff == "-":  # Для случая "-x^2"
                    coeff = "-1"
                degree = degree if degree else "1"
                self.add_term(Natural(degree), Rational(Integer(coeff)))
            else:
                self.add_term(Natural("0"), Rational(Integer(term)))

def create_polynomial(input_str: str) -> Polynomial:
    """
    Утилита для создания многочлена из строки.

    :param input_str: Строка, представляющая многочлен.
    :return: Экземпляр Polynomial.
    """
    poly = Polynomial()
    poly.build_from_string(input_str)
    return poly


