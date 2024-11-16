import tkinter as tk
from tkinter import ttk, messagebox
from operations.natural_operations import NaturalOperations
from operations.integer_operations import IntegerOperations
from operations.rational_operations import RationalOperations
from operations.polynomial_operation import PolynomialOperations

# Функция обработки выбора модуля
def execute_module(module_name):
    messagebox.showinfo("Выполнение", f"Вы выбрали модуль: {module_name}")


# Основной класс приложения
class AlgebraSystemApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система компьютерной алгебры")
        self.geometry("800x600")

        # Категории и модули
        self.categories = {
            "Натуральные числа с нулем": {
                "N-1 Сравнение натуральных чисел": NaturalOperations.COM_NN_D,
                "N-2 Проверка на ноль": NaturalOperations.NZER_N_B,
                "N-3 Добавление 1 к натуральному числу": NaturalOperations.ADD_1N_N,
                "N-4 Сложение натуральных чисел": NaturalOperations.ADD_NN_N,
                "N-5 Вычитание из первого большего натурального числа второго меньшего или равного": NaturalOperations.SUB_NN_N,
                "N-6 Умножение натурального числа на цифру": NaturalOperations.MUL_ND_N,
                "N-7 Умножение натурального числа на 10^k, k-натуральное": NaturalOperations.MUL_Nk_N,
                "N-8 Умножение натуральных чисел": NaturalOperations.MUL_NN_N,
                "N-9 Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом": NaturalOperations.SUB_NDN_N,
                "N-10 Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k": NaturalOperations.DIV_NN_Dk,
                "N-11 Неполное частное от деления первого натурального числа на второе с остатком": NaturalOperations.DIV_NN_N,
                "N-12 Остаток от деления первого натурального числа на второе натуральное": NaturalOperations.MOD_NN_N,
                "N-13 НОД натуральных чисел": NaturalOperations.GCF_NN_N,
                "N-14 НОК натуральных чисел": NaturalOperations.LCM_NN_N,
            },
            "Целые числа": {
                "Z-1 Абсолютная величина числа": IntegerOperations.ABS_Z_N,
                "Z-2 Определение положительности числа": IntegerOperations.POZ_Z_D,
                "Z-3 Умножение целого на (-1)": IntegerOperations.MUL_ZM_Z,
                "Z-4 Преобразование натурального в целое": IntegerOperations.TRANS_N_Z,
                "Z-5 Преобразование целого неотрицательного в натуральное": IntegerOperations.TRANS_Z_N,
                "Z-6 Сложение целых чисел": IntegerOperations.ADD_ZZ_Z,
                "Z-7 Вычитание целых чисел": IntegerOperations.SUB_ZZ_Z,
                "Z-8 Умножение целых чисел": IntegerOperations.MUL_ZZ_Z,
                "Z-9 Частное от деления целого на целое": IntegerOperations.DIV_ZZ_Z,
                "Z-10 Остаток от деления целого на целое": IntegerOperations.MOD_ZZ_Z,
            },
            "Рациональные числа": {
                "Q-1 Сокращение дроби",
                "Q-2 Проверка сокращенного дробного на целое",
                "Q-3 Преобразование целого в дробное",
                "Q-4 Преобразование сокращенного дробного в целое",
                "Q-5 Сложение дробей",
                "Q-6 Вычитание дробей",
                "Q-7 Умножение дробей",
                "Q-8 Деление дробей (делитель отличен от нуля)",
            },
            "Многочлены с рациональными коэффициентами": {
                "P-1 Сложение многочленов",
                "P-2 Вычитание многочленов",
                "P-3 Умножение многочлена на рациональное число",
                "P-4 Умножение многочлена на x^k, k-натуральное или 0",
                "P-5 Старший коэффициент многочлена",
                "P-6 Степень многочлена",
                "P-7 Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей",
                "P-8 Умножение многочленов",
                "P-9 Частное от деления многочлена на многочлен при делении с остатком",
                "P-10 Остаток от деления многочлена на многочлен при делении с остатком",
                "P-11 НОД многочленов",
                "P-12 Производная многочлена",
                "P-13 Преобразование многочлена — кратные корни в простые",
            },
        }

        # Создаем интерфейс
        self.create_widgets()

    def create_widgets(self):
        # Создание выпадающего списка категорий
        self.category_label = tk.Label(self, text="Выберите категорию:")
        self.category_label.pack(pady=10)

        self.category_combobox = ttk.Combobox(self, values=list(self.categories.keys()))
        self.category_combobox.pack(pady=10)
        self.category_combobox.bind("<<ComboboxSelected>>", self.on_category_selected)

        # Список модулей
        self.module_label = tk.Label(self, text="Модули:")
        self.module_label.pack(pady=10)

        self.module_listbox = tk.Listbox(self, height=15)
        self.module_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Кнопка для выполнения модуля
        self.execute_button = tk.Button(self, text="Выполнить", command=self.on_execute)
        self.execute_button.pack(pady=10)

    def on_category_selected(self, event):
        category = self.category_combobox.get()
        self.module_listbox.delete(0, tk.END)
        for module in self.categories[category]:
            self.module_listbox.insert(tk.END, module)

    def on_execute(self):
        selected_module = self.module_listbox.get(tk.ACTIVE)
        if selected_module:
            execute_module(selected_module)
        else:
            messagebox.showwarning("Ошибка", "Выберите модуль для выполнения.")

# Запуск приложения
if __name__ == "__main__":
    app = AlgebraSystemApp()
    app.mainloop()

