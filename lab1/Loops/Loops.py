# У вас есть список из целых чисел и еще один пустой список.
# Вам нужно пройти по заполненному списку циклом и записать в пустой список все четные значения
import random

def first_task():
    first_list = []
    second_list=[]
    n = 10
    for i in range(n):
        first_list.append(random.randint(-100, 100))
    print(f"Первый список = {first_list}")
    for i in first_list:
        if i % 2 == 0:
            second_list.append(i)
    print(f"Второй список = {second_list}")

first_task()