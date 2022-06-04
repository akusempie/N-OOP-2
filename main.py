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

    def rate_lecturer(self, lecturer, course, lecture, grade):
        if (isinstance(lecturer, Lecturer) and course in Lecturer.courses_attached
                and course in self.courses_in_progress and lecture in Lecturer.lectures):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[lecture] = [grade]
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.lectures = []


class Lecturer(Mentor):

    def lect(self):
        pass


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Rick', 'Sanchez')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.lectures += ['Python in Data Science']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_lecturer.grades(best_student, 'Python in Data Science', 10)


print(best_student.grades)
print(cool_lecturer.grades)