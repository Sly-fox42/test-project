# Списки - Практика


# Задание
# Напишите программу, которая запрашивает у пользователя оценки (целые числа) для 5 студентов,
# сохраняет их в список и выводит среднюю оценку по классу.
# Также программа должна определить и вывести самую высокую и самую низкую оценку.


# Пример работы программы:

# Введите оценку студента 1: 85
# Введите оценку студента 2: 90
# Введите оценку студента 3: 78
# Введите оценку студента 4: 92
# Введите оценку студента 5: 88
#
# Средняя оценка: 86.6
# Самая высокая оценка: 92
# Самая низкая оценка: 78


# Темы:
#   - Функции input() и print() (lesson10)
#   - Условные операторы - if-else (lesson16)
#   - Цикл for (lesson18)
#   - Списки (lesson19)

# Ваше решение:

student1_estimation1=int(input("Введите оценку студента 1: "))
student1_estimation2=int(input("Введите оценку студента 2: "))
student1_estimation3=int(input("Введите оценку студента 3: "))
student1_estimation4=int(input("Введите оценку студента 4: "))
student1_estimation5=int(input("Введите оценку студента 5: "))
student1_estimation =[student1_estimation1,student1_estimation2,student1_estimation3,student1_estimation4,student1_estimation5]
sum_est =0
if 0>=student1_estimation1 or student1_estimation2 or student1_estimation3 or student1_estimation4 or student1_estimation5 <=100:
    for item in student1_estimation:
         sum_est+=item
else:
    print("Вы ввели неверные данные ")
print(f"Средняя оценка: {(sum_est/len(student1_estimation))}")

print(f"Самая низкая оценка: {min(student1_estimation)}")
print(f"Самая высокая оценка: {max(student1_estimation)}")
