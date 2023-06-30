from Human import Human


class Teacher(Human):
    all_teachers = []

    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        super().__init__(name, surname, email, age, tel)
        self.all_teachers.append(self)
