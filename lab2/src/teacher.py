from lab2.src.human import Human


class Teacher(Human):
    all_teachers = []

    def __init__(self, name: str, surname: str, email: str, age: int, tel: str):
        super().__init__(name, surname, email, age, tel)
        self.all_teachers.append(self)

    @staticmethod
    def get_all_teachers() -> list:
        return Teacher.all_teachers

    @staticmethod
    def check_teacher(teacher) -> bool:
        return teacher in Teacher.all_teachers

    def hold_lesson(self, lesson, students: list) -> bool:
        if self.check_teacher(self):
            if lesson.check_teacher_by_lesson(self):
                student_names = []
                for stud in students:
                    student_names.append(stud.name)
                    stud.get_knowledge(lesson)
                print(f"Преподаватель {self.surname} {self.name} провел занятие \"{lesson.lesson_name}\" \n  "
                      f"Для студентов: \n{student_names}")
                return True
            return False
        return False
