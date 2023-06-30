from lab2.src.Human import Human


class Student(Human):
    all_students = []

    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        self.knowledge = []
        super().__init__(name, surname, email, age, tel)
        self.all_students.append(self)

    @classmethod
    def get_all_students(cls) -> list:
        return cls.all_students

    @classmethod
    def check_student(cls, student) -> bool:
        return student in cls.all_students

    def get_knowledge(self, lesson) -> bool:
        try:
            self.knowledge.append(lesson)
            return True
        except BaseException:
            return False
