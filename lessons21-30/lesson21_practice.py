# Функции range и enumerate - Практика


# Задание
# Создайте список из 7 названий книг.
# Выведите список книг, начиная нумерацию с 1.
# Удалите из списка все книги, у которых длина названия больше 15 символов.
# Добавьте две новые книги в конец списка.
# Сортируйте список по длине названия книг.
# Выведите итоговый список.


# Пример работы программы:


# Список книг:
# 1. Гарри Поттер
# 2. Марсианские бои
# 3. Властелин Колец
# 4. Таинственный остров
# 5. Хроники Нарнии
# 6. Стражи Галактики
# 7. Одиссея
#
# Список книг, у которых название длиннее 15 символов:
# 1. Гарри Поттер
# 2. Марсианские бои
# 3. Властелин Колец
# 4. Хроники Нарнии
# 5. Одиссея
#
# Напишите названия 2 новых книг через запятую: 1984, Атомные привычки
#
# Список книг, отсортированный по длине названия:
# 1. 1984
# 2. Одиссея
# 3. Гарри Поттер
# 4. Хроники Нарнии
# 5. Марсианские бои
# 6. Властелин Колец
# 7. Атомные привычки


# Темы:
#   - Функции input() и print() (lesson10)
#   - Циклы for (lesson18)
#   - Списки (lesson19)
#   - Методы списков (lesson20)
#   - Функции range и enumerate (lesson21)


# Ваше решение:

print("Введите 7 последних прочитанных вами книг")
books = []

for i in range(7):
    book = input("Введите название книги: ")
    books.append(book)

print("Список книг:")
for i, a_book in enumerate(books):

    print(f"{i + 1}. {a_book}")

print("Список книг, у которых название длиннее 15 символов: ")
for i in books:
    if len(i)>15:
        books.remove(i)
        print(i)