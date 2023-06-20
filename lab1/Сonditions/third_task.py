find_letter = "Е"
text = str(input("Введите строку: "))

if find_letter.upper().lower() in text.upper().lower():
    print(f"Буква '{find_letter}' есть в тексте")
else:
    print(f"Буквы '{find_letter}' нет в тексте")