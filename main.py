class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg(self, grades):
        avgdict = {}
        for course, grade in self.grades.items():
            avgdict[course] = sum(grade) / len(grade)
        return avgdict

    def __str__(self):
        self.averages = self.avg(self.grades)
        self.average_of_averages = sum(self.averages.values()) / len(self.averages)

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.average_of_averages, 1)}\n' \
               f'Курсы в процессе изучения: {", ".join(str(x) for x in self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(str(x) for x in self.finished_courses)}'

    def __lt__(self, other):
        return self.average_of_averages < other.average_of_averages

    def __gt__(self, other):
        return self.average_of_averages > other.average_of_averages


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}

    def avg(self, grades):
        avgdict = {}
        for course, grade in self.grades.items():
            avgdict[course] = sum(grade) / len(grade)
        return avgdict

    def __str__(self):
        self.averages = self.avg(self.grades)
        self.average_of_averages = sum(self.averages.values()) / len(self.averages)

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.average_of_averages, 1)}'

    def __lt__(self, other):
        return self.average_of_averages < other.average_of_averages

    def __gt__(self, other):
        return self.average_of_averages > other.average_of_averages


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# называем студентов и записываем на курс

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
grading_student = Student('Morty', 'Sanchez', 'male')
grading_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

# называем определенного ревьювера и назначаем ему курс

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']

# называем определенного лектора и назначаем ему курс

cool_lecturer = Lecturer('Rick', 'Sanchez')
cool_lecturer.courses_attached += ['Python', 'Git']
regular_lecturer = Lecturer('Rose', 'Fibonacci')
regular_lecturer.courses_attached += ['Python', 'Git']

# ставим оценки студенту

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(grading_student, 'Python', 10)
cool_mentor.rate_hw(grading_student, 'Git', 10)
cool_mentor.rate_hw(grading_student, 'Git', 5)

# ставим оценки лектору

grading_student.rate_lecturer(cool_lecturer, 'Python', 10)
grading_student.rate_lecturer(cool_lecturer, 'Git', 9)
grading_student.rate_lecturer(regular_lecturer, 'Python', 8)
best_student.rate_lecturer(regular_lecturer, 'Git', 5)


# Функция сравнения оценок студентов или преподавателей


def compare(first_person, second_person):
    if first_person.average_of_averages > second_person.average_of_averages:
        return True
    else:
        return False


students_list = [best_student.grades, grading_student.grades]
lecturers_list = [cool_lecturer.grades, regular_lecturer.grades]


def avg_student_grades(students, course_name):
    average = {}
    for student in students:
        for course, grade in student.items():
            if course == course_name:
                average[course] = (sum(grade) / len(grade))

                return f'Средняя оценка у всех студентов по курсу {course}: {round(average[course], 1)}'


print(grading_student, best_student, sep='\n')
print(cool_lecturer, regular_lecturer, cool_mentor, sep='\n')
# Сравнить средние оценки, если лучше у первого студента или преподавателя, то True
print(compare(first_person=best_student, second_person=grading_student))
print(avg_student_grades(students_list, course_name='Python'))

# Реализация методов __lt__, __gt__
is_student_lt = (best_student < grading_student)
is_student_gt = (best_student > grading_student)
print(is_student_lt)
print(is_student_gt)
