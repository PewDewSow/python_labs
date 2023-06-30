class Worker:
    def __init__(self, fio='Some Name', tel='Some tel', post='Some pos', department='Some dep', salary=1111):
        self.fio = fio
        self.tel = tel
        self.post = post
        self.department = department
        self.salary = salary

    def get_fio(self):
        return self.fio

    def get_post(self):
        return self.post

    def get_tel(self):
        return self.tel

    def set_fio(self, fio):
        self.fio = fio

    def set_post(self, post):
        self.post = post

    def set_tel(self, tel):
        self.tel = tel
