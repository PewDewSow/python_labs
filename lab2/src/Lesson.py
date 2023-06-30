from .Teacher import Teacher


class Lesson:
    all_lessons = []

    def __init__(self, lesson_name: str, theme: str, teachers: list):
        self.lesson_name = lesson_name
        self.theme = theme
        self.teachers = teachers
        self.all_lessons.append(self)

    def check_teacher_by_lesson(self, teacher: Teacher) -> bool:
        if self in teacher:
            return True
        else:
            print(f"Преподаватель {teacher.surname} {teacher.name} не "
                  f"может преподать урок \"{self.name}\", так как не знает его")
            return False

    def get_teachers_by_lesson(self):
        return self.teachers
