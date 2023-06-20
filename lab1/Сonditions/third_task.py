# Проверить есть ли в произвольной строке буква «Е»
find_letter = "Е"
text = str(input("Введите строку: "))

if find_letter.lower() in text.lower():
    print(f"Буква '{find_letter}' есть в тексте")
else:
    print(f"Буквы '{find_letter}' нет в тексте")