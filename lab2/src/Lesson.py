class Lesson:
    all_lessons = []

    def __init__(self, lesson_name: str, theme: str, teachers: list):
        self.lesson_name = lesson_name
        self.theme = theme
        self.teachers = teachers
        self.all_lessons.append(self)

    def check_teacher_by_lesson(self, teacher) -> bool:
        if teacher in self.teachers:
            return True
        else:
            print(f"Преподаватель {teacher.surname} {teacher.name} не "
                  f"может преподать урок \"{self.lesson_name}\", так как не знает его")
            return False

    def get_teachers_by_lesson(self) -> list:
        return self.teachers
