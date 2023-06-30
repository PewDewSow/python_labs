import src

Teacher_Vladislav = src.Teacher('Vladislav', 'Vlad_surname', 'vlad@gmail.com', 25, '1684')
Teacher_Alexey = src.Teacher('Alexey', 'Alex_surname', 'alex@gmail.com', 30, '1314')

Stud_Vitya = src.Student('Vitya', 'Vitya_surname', 'vitya@gmail.com', 17, '7867687')
Stud_Dima = src.Student('Dima', 'Dima_surname', 'dima@gmail.com', 17, '525324')
Stud_Anna = src.Student('Anna', 'Anna_surname', 'anna@gmail.com', 17, '432523')
Stud_Sasha = src.Student('Sasha', 'Sasha_surname', 'sasha@gmail.com', 17, '634634')

Less_Programming = src.Lesson('Programming', 'Программирование', [Teacher_Vladislav])
Less_Music = src.Lesson('Music', 'Музыка', [Teacher_Alexey])
