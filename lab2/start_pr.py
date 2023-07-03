from src.lesson import Lesson
from src.student import Student
from src.teacher import Teacher

Teacher_Vladislav = Teacher('Vladislav', 'Vlad_surname', 'vlad@gmail.com', 25, '1684')
Teacher_Alexey = Teacher('Alexey', 'Alex_surname', 'alex@gmail.com', 30, '1314')

Stud_Vitya = Student('Vitya', 'Vitya_surname', 'vitya@gmail.com', 17, '7867687')
Stud_Dima = Student('Dima', 'Dima_surname', 'dima@gmail.com', 17, '525324')
Stud_Anna = Student('Anna', 'Anna_surname', 'anna@gmail.com', 17, '432523')
Stud_Sasha = Student('Sasha', 'Sasha_surname', 'sasha@gmail.com', 17, '634634')

Less_Programming = Lesson('Programming', 'Программирование', [Teacher_Vladislav])
Less_Music = Lesson('Music', 'Музыка', [Teacher_Alexey])

Teacher_Vladislav.hold_lesson(Less_Programming, [Stud_Sasha, Stud_Dima, Stud_Vitya])
Teacher_Alexey.hold_lesson(Less_Music, [Stud_Anna])

Teacher_Alexey.hold_lesson(Less_Programming, [Stud_Vitya])
