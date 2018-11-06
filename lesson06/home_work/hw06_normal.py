# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    @property
    def name(self):
        return ' ' \
               '"{}"'.format(self._school_name)

    @property
    def adress(self):
        return '{}'.format(self._school_adress)


class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)

    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mather': mather,
            'father': father
            }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


teachers = [
    Teacher('Жукова', 'Людмила', 'Александровна', 'Математика',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Белик', 'Вячеслав', 'Валерьевич', 'Информатика',
            ['10А', '10Б', '11А', '11Б']),
    Teacher('Лакина', 'Надежда', 'Фёдоровна', 'История',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Мордвинова', 'Татьяна', 'Владимировна', 'Литература',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Лагута', 'Татьяна', 'Ивановна', 'География',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б'])
    ]

students = [
    Student('Ковалев', 'Александр', 'Александрович', '10Б',
            'Ковалева О. А.', 'Ковалев А. В.'),
    Student('Юдин', 'Евгений', 'Алексеевич', '11А',
            'Юдина Т.В.', 'Юдин А.В.'),
    Student('Бахрушин', 'Константин', 'Сергеевич', '11Б',
            'Бахрушина А.Д.', 'Бахрушин С.А.'),
    Student('Звонарев', 'Виталий', 'Николаевич', '10А',
            'Звонарева А.К.', 'Звонарев Н.В.'),
    Student('Ю Тань', 'Артём', 'Александрович', '9Б',
            'Ю Таньа В.А.', 'Ю Тань А.Т'),
    Student('Котиков', 'Никита', 'Никитович', '9А',
            'Котикова Н.А.', 'Котиков Н.С.'),
    Student('Савельева', 'Дарья', 'Александровна', '8Б',
            'Савельева А.В.', 'Савельев А.С.'),
    Student('Штемц', 'Андрей', 'Васильевич', '8А',
            'Штемц Е.В.', 'Штемц В.С.'),
    Student('Андреева', 'Анна', 'Владимировна', '7Б',
            'Андреева А.Д.', 'Андреев В.А.'),
    Student('Зайцев', 'Михаил', 'Аркадьевич', '7А',
            'Зайцева А.Г.', 'Зайцев А.С.'),
    Student('Кулебякин', 'Александр', 'Сергеевич', '10Б',
            'Кулебякина О. А.', 'Кулебякин С. В.'),
    Student('Кулебякин', 'Алексей', 'Сергеевич', '11А',
            'Кулебякина О. А.', 'Кулебякин С. В..'),
    Student('Макарова', 'Ирина', 'Александровна', '11Б',
            'Макарова А.Д.', 'Макаров А.А.'),
    Student('Кравченко', 'Александр', 'Владимирович', '10А',
            'Кравченко Е.К.', 'Кравченко В.В.'),
    Student('Беляева', 'Мария', 'Вячеславовна', '9Б',
            'Беляева В.А.', 'Беляев В.Т'),
    Student('Рыбакова', 'Лидия', 'Константиновна', '9А',
            'Рыбакова Н.А.', 'Рыбаков К.С.'),
    Student('Абрамкин', 'Ярослав', 'Александрович', '8Б',
            'Абрамкина А.В.', 'Абрамкин А.С.'),
    Student('Кудякова', 'Анжелла', 'Васильевна', '8А',
            'Кудякова Е.В.', 'Кудяков В.С.'),
    Student('Дмитриева', 'Лилия', 'Владимировна', '7Б',
            'Дмитриева А.Д.', 'Дмитриев В.А.'),
    Student('Андросова', 'Анна', 'Сергеевна', '7А',
            'Андросова А.Г.', 'Андросов С.С.'),
    ]


school = School('Школа Питона №1,', 'Луна, '
                'Море Спокойствия', teachers, students)

print(school.name)
print(school.adress)

print('\nСписок классов школы:')
print(', '.join(school.get_all_classes()))

print('\nСписок "10Б" класса:')
print('\n'.join(school.get_students('10Б')))

student = school.find_student('Ковалев Александр Александрович')
print('\nУченик: {0}\nУчебный класс: "{1}"\n'
      'Учителя: {2}\nПредметы: {3}'.format(student['full_name'],
                                           student['class_room'],
                                           ', '.join(student['teachers']),
                                           ', '.join(student['lessons'])))

print('Родители: {0}, {1}'.format(student['parents']['mather'],
                                   student['parents']['father']))

print('\nКласс: "8А"\nПреподаватели: '
      '{0}'.format(', '.join(school.get_teachers('8А'))))