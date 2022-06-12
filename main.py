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
        averages = self.avg(self.grades)
        average_of_averages = sum(averages.values())/len(averages)

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(average_of_averages,1)}\n' \
               f'Курсы в процессе изучения: {", ".join(str(x) for x in self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(str(x) for x in self.finished_courses)}'

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
        averages = self.avg(self.grades)
        average_of_averages = sum(averages.values())/len(averages)

        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(average_of_averages,1)}'


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
best_student.courses_in_progress += ['Python']
grading_student = Student('Morty', 'Sanchez', 'male')
grading_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']



# называем определенного ревьювера и назначаем ему курс

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# называем определенного лектора и назначаем ему курс

cool_lecturer = Lecturer('Rick', 'Sanchez')
cool_lecturer.courses_attached += ['Python', 'Git']

# ставим оценки студенту

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 5)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(grading_student, 'Python', 10)


# ставим оценки лектору

grading_student.rate_lecturer(cool_lecturer, 'Python', 10)
grading_student.rate_lecturer(cool_lecturer, 'Git', 9)



print(best_student.grades)
print(cool_lecturer.grades)
print(grading_student, best_student, sep='\n')
print(cool_lecturer, cool_mentor, sep='\n')

