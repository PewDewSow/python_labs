first_dict = {
    'name': 'Denis',
    'surname': 'Kosinov',
    'gender': 'male',
    'age': '26',
    'status': 'student'
}

first_list = ['gender', 'nobody', 'status']

# Пройти по словарю и вывести значения всех ключей
def get_keys():
    for i in first_dict.keys():
        print(i)

# Пройти по словарю и вывести ключи через один
def get_keys_second():
    count = 0
    for i in first_dict.keys():
        if count % 2 == 0:
            print(i)
        count += 1

# Узнать есть ли в словаре определенный ключ
def is_key_exist():
    key_find = 'name'
    if key_find in first_dict.keys():
        print(f"Ключ '{key_find}' есть в словаре.")

# Узнать есть ли в словаре ключ с определенным значением
def is_value_exist():
    value_find = 'Denis'
    for key, value in first_dict.items():
        if value_find == value:
            print(f"Ключ '{key}' со значением {value_find} есть в словаре.")


# Узнать есть ли в словаре определенный ключ с определенным значением
def is_value_and_key_exist():
    value_find = '26'
    key_find = 'age'
    for key, value in first_dict.items():
        if value_find == value and key_find == key:
            print(f"Ключ '{key_find}' со значением {value_find} есть в словаре.")


# У вас есть словарь и список. В списке содержится часть элементов Словаря. Вам нужно пройти циклом по списку
# и вывести значение словаря, если такой ключ существует
def check_list_in_dict():
    for i in first_list:
        if i in first_dict.keys():
            print(f"Ключ '{i}' со значением {first_dict[i]} есть в словаре.")

check_list_in_dict()