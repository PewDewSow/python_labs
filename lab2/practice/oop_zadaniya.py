from lab2.practice.helper import *

Vitya = Worker('Vitya Ivanov', '+1234-567-8989', 'Manager', 'Sales', 15000)
Misha = Worker('Misha Ivanov', '+1234-567-1212', 'Admin', 'IT', 10000)
Jel = Helper('Jel Ivanov', '+1234-567-121452', 'Helper', 'Sales', 2000)

print(Vitya.get_fio())

print(Misha.get_fio())
print(Misha.get_tel())
print(Misha.get_post())

Jel.get_boss()
