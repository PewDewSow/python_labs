# Проверить есть ли в произвольной строке, хотя бы одна из букв А Б В
first_find_letter, second_find_letter, third_find_letter = 'А', 'Б', 'В'
text = str(input("Введите строку: "))

if first_find_letter.lower() in text.lower():
    print(f"Буква '{first_find_letter}' есть в тексте")
elif second_find_letter.lower() in text.lower():
    print(f"Буква '{second_find_letter}' есть в тексте")
elif third_find_letter.lower() in text.lower():
    print(f"Буква '{third_find_letter}' есть в тексте")
else:
    print("Букв '{0}, {1}, {2}' нет в тексте".format(first_find_letter, second_find_letter, third_find_letter))