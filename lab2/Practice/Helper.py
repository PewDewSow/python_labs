from lab2.Practice.Worker import *


class Helper(Worker):
    def __init__(self, fio='Some Name', tel='Some tel', post='Some pos', department='Some dep', salary=1111,
                 boss: Worker = None):
        self.boss = boss
        super().__init__(fio, tel, post, department, salary)

    def get_boss(self):
        return print(f"My boss is {self.boss.fio}") if self.boss is not None else print("Sry, I don't have a boss")

    def set_boss(self, boss: Worker):
        self.boss = boss
