from Human import Human
from Lesson import Lesson
from Student import Student


class Teacher(Human):
    all_teachers = []

    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        super().__init__(name, surname, email, age, tel)
        self.all_teachers.append(self)

    @staticmethod
    def get_all_teachers() -> list:
        return all_teachers

    @staticmethod
    def check_teacher(teacher: Teacher) -> bool:
        return True if teacher in all_teachers else False

    def hold_lesson(self, lesson: Lesson, students: list[Student]) -> bool:
        if self.check_teacher(self):
            if lesson.check_teacher_by_lesson(self):
                student_names = []
                for stud in students:
                    student_names.append(stud.name)
                    stud.get_knowledge(lesson)
                print(f"Преподаватель {self.surname} {self.name} провел занятие \"{lesson.name}\" \n  "
                      f"Для студентов: \n{student_names}")
                return True
            return False
        return False
