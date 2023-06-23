first_dict = {
    'name': 'Denis',
    'surname': 'Kosinov',
    'gender': 'male',
    'age': '26',
    'status': 'student'
}

first_list = ['gender', 'nobody', 'status']

def get_keys():
    for i in first_dict.keys():
        print(i)

def get_keys_second():
    count = 0
    for i in first_dict.keys():
        if count % 2 == 0:
            print(i)
        count += 1

def is_key_exist():
    key_find = 'name'
    if key_find in first_dict.keys():
        print(f"Ключ '{key_find}' есть в словаре.")

def is_value_exist():
    value_find = 'Denis'
    for key, value in first_dict.items():
        if value_find == value:
            print(f"Ключ '{key}' со значением {value_find} есть в словаре.")

def is_value_and_key_exist():
    value_find = '26'
    key_find = 'age'
    for key, value in first_dict.items():
        if value_find == value and key_find == key:
            print(f"Ключ '{key_find}' со значением {value_find} есть в словаре.")

def check_list_in_dict():
    for i in first_list:
        if i in first_dict.keys():
            print(f"Ключ '{i}' со значением {first_dict[i]} есть в словаре.")

check_list_in_dict()