# Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран,
# сообщая об ошибке в случае деления на ноль

first_value = float(input("Введите первое число: "))
second_value = float(input("Введите второе число: "))

try:
    print(f"{first_value} / {second_value} = {first_value / second_value}")
except ZeroDivisionError:
    print("Делить на 0 нельзя!")