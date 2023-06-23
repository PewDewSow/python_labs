# У вас есть список из целых чисел и еще один пустой список.
# Вам нужно пройти по заполненному списку циклом и записать в пустой список все четные значения
import random


def first_task():
    first_list = []
    second_list = []
    n = 10
    for i in range(n):
        first_list.append(random.randint(-100, 100))
    else:
        print(f"Первый список = {first_list}")
    for i in first_list:
        if i % 2 == 0:
            second_list.append(i)
    else:
        print(f"Второй список = {second_list}")


# У вас есть строка, нужно пройти по каждому символу и, если он цифра – вывести его
def second_task():
    text = "sajdgh312r98tdfbaskj314123sdads"
    text_final = ''
    for i in text:
        if i.isdigit():
            text_final += i
    else:
        print(text_final)


# Пройдите по строке циклом и продублируйте каждый ее символ 3 раза. Выведите итоговую строку
def third_task():
    text = "stroka!"
    text_final = ''
    print(f"Исходная строка = {text}")
    for i in text:
        text_final += i * 3
    else:
        print(f"Финальная строка = {text_final}")


# Определите, не является ли введенная пользователем с клавиатуры строка пустой. Результат проверки в
# виде True или False выведите на экран.
def fourth_task():
    text = str(input("Введите строку: "))
    if text != '':
        print("True")
    else:
        print("False")


# Напишите программу, которая из предоставленного списка целых значений возвращает (печатает) только Чётные
def fifth_task():
    first_list = []
    n = 10
    for i in range(n):
        first_list.append(random.randint(-100, 100))
    else:
        print(f"Первый список = {first_list}")
    for i in first_list:
        if i % 2 == 0:
            print(i)


# Напишите программу, которая из предоставленного списка целых значений возвращает (печатает) только Чётные.
# НЕ четные увеличивает на 1 и выводит.
def sixth_task():
    first_list = []
    n = 10
    for i in range(n):
        first_list.append(random.randint(-100, 100))
    else:
        print(f"Первый список = {first_list}")
    for i in first_list:
        print(i + 1 if i % 2 != 0 else i)

# У вас есть список любых значений (целые числа) вывести только положительные
def seventth_task():
    first_list = []
    n = 10
    for i in range(n):
        first_list.append(random.randint(-100, 100))
    else:
        print(f"Первый список = {first_list}")
    for i in first_list:
        if i > 0:
            print(i)

seventth_task()