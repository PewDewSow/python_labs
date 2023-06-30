from Lesson import Lesson


class Student:
    all_students = []

    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        self.knowledge = []
        super().__init__(name, surname, email, age, tel)
        self.all_students.append(self)

    @staticmethod
    def get_all_students() -> list:
        return all_students

    @staticmethod
    def check_student(student: Student) -> bool:
        return True if student in all_students else False

    def get_knowledge(self, lesson: Lesson) -> bool:
        try:
            self.knowledge.append(lesson)
            return True
        except BaseException:
            return False
