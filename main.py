class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_courses(self, course_name):
            self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


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


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# называем лучшего студента и записываем его на курс

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# называем определенного ревьювера и назначаем ему курс

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# называем определенного лектора и назначаем ему курс

cool_lecturer = Lecturer('Rick', 'Sanchez')
cool_lecturer.courses_attached += ['Python', 'Git']

# ставим оценки студенту

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

# ставим оценки лектору

grading_student = Student('Morty', 'Sanchez', 'male')
grading_student.courses_in_progress += ['Python', 'Git']
grading_student.rate_lecturer(cool_lecturer, 'Python', 10)
grading_student.rate_lecturer(cool_lecturer, 'Git', 10)



print(best_student.grades)
print(cool_lecturer.grades)