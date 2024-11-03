# Цикл for - Практика
from itertools import count

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
# else:
#     for a1 in range(1, (int(size)+1)//2 + 1): #from row 1 to 5
#         for a2 in range((int(size)+1)//2 - a1):
#             print(" ", end = "")
#         for a3 in range((a1*2)-1):
#             print("*", end = "")
#         print()
#
#     for a1 in range((int(size)+1)//2 + 1,int(size) + 1): #from row 6 to 9
#         for a2 in range(a1 - (int(size)+1)//2):
#             print(" ", end = "")
#         for a3 in range((int(size)+1 - a1)*2 - 1):
#             print("*", end = "")
#         print()
min_size =3
count1 =1
count2 =1
for i in range(min_size,int(size)):
    for j in (min_size,size):
        print(" "*(min_size+count1)+"*"*count2)
        count1-=1
        count2+=2
    if count2 ==int(size):
        for k in range(min_size, int(size)):
            for l in (min_size, size):
                print(" " * (min_size + count1) + "*" * count2)
                count1 += 1
                count2 -= 2
