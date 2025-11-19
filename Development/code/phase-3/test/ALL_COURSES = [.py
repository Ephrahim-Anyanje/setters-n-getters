ALL_COURSES = [
    "Data Science",
    "Software Engineering",
    "DevOPS",
    "Cyber Security",
    "AI Engineering",
    "High School Bootcamp",
    "Product Design",
    "Data Analytics",
    "Data Analytics for HR Professionals",
]


class Student:
    student_count = 0
    all_students = []

    def __init__(self, first_name, last_name, age, gender, student_id, course, instructor):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.course = course
        self.instructor = instructor

        Student.student_count += 1
        Student.all_students.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError("First name must be a string")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str):
            self._last_name = value
        else:
            raise ValueError("Last name must be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 18:
            self._age = value
        else:
            raise ValueError("Student must be 18 or older to join")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if isinstance(value, str) and value.lower() in ("male", "female"):
            self._gender = value.capitalize()
        else:
            raise ValueError("Gender must be 'Male' or 'Female'")


    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course in ALL_COURSES:
            self._course = course
        else:
            raise ValueError("The course listed is not available yet")

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    

    @classmethod
    def total_students(cls):
        return f"The total number of students is: {cls.student_count}"

    @classmethod
    def student_list(cls):
        return [student.fullname for student in cls.all_students]

    @classmethod
    def student_list_2(cls):
        return [student.fullname for student in cls.all_students]

    @staticmethod
    def reverse_name(first_name, last_name):
        return f"{last_name} {first_name}"
