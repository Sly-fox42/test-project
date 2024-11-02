# Цикл for - Практика


# Задание
# Напишите программу, которая нарисует в консоли ромбик из звездочек c одинаковыми по длине сторонами.
# Сначала пользователь должен ввести размер ромбика (НЕЧЕТНОЕ ЧИСЛО от 3 до 15).
# Если значение
#   - или не является числом;
#   - или не входит в диапазон;
#   - или является ЧЕТНЫМ,
#   то вывести сообщение об ошибке: "Некорректное значение!"
# Если значение входят в диапазон, то вывести ромбик.


# Пример вывода в консоль:

# Эта программа рисует ромбик
#
# Введите размер ромбика.
# Размер должен быть нечетным числом от 3 до 15: 7
#
# Ваш ромбик:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


# Темы:
#   - Преобразование типов данных (lesson6),
#   - Сравнение чисел (lesson8),
#   - Функции input() и print() (lesson10)
#   - Условные операторы - if-else (lesson16)
#   - Цикл for (lesson18)


# Ваше решение:
print("Эта программа рисует ромбик")
size = input("Введите размер ромбика: ")
print("Размер должен быть нечетным числом от 3 до 15: 7\nВаш ромбик:")
if not size.isdigit() or 3<int(size)>=15 or int(size)%2 == 0:
    print("Некорректное значение!")
