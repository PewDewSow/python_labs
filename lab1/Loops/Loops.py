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


second_task()
