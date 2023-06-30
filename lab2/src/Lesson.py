class Lesson:
    all_lessons = []

    def __init__(self, lesson_name: str, theme: str, teachers: list):
        self.lesson_name = lesson_name
        self.theme = theme
        self.teachers = teachers
