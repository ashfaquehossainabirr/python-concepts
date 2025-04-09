# Class methods = Allow operations related to the class
#                 Take (cls) as the first parameter, which represents the class itself.

#  Instance methods = Best for operations on instances of the class (objects)
#  Static methods = Best for utility functions that do not need access to class data
#  Class methods = Best for class-level data or require access to the class itself


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total No. of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return f"Average GPA: {0}"
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


print(Student.get_count())

student1 = Student("Spongebob", 3.53)
student2 = Student("Patrick", 3.16)
student3 = Student("Sandy", 3.92)

print(Student.get_count())
print(Student.get_average_gpa())