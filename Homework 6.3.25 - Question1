import copy
from abc import ABC, abstractmethod


class IClone(ABC):
    @abstractmethod
    def clone(self):
        pass

class Student(IClone):
    def __init__(self, name:str, id:str, grades:dict[int, float], is_active:bool):
        self.name = name
        self.id = id
        self.grades = grades
        self.is_active = is_active

    def add_grade(self, course_id:int, grade:float):
        self.grades[course_id] = grade

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values())/len(self.grades)
        else:
            return 0.0

    def toggle_active_status(self):
        self.is_active = not self.is_active

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Student(name ={self.name}, id = {self.id}, grades = {self.grades}, is_active = {self.is_active})"

original_student = Student("Moshe", "996415233", {19:83.2, 21:72.1,93:88.8}, True)
cloned_student = original_student.clone()


cloned_student.grades = {11:91.2,23:74.4,13:57.0}
cloned_student.name = cloned_student.name.replace(original_student.name,"Avi")
cloned_student.id = cloned_student.id.replace(original_student.id, "223417659")
cloned_student.add_grade(15, 24)



print("Original Student:", original_student)
print("Cloned Student:", cloned_student)
print("Original Student's average grade is", original_student.get_average_grade())
print("Cloned Student's average grade is", cloned_student.get_average_grade())
print(cloned_student.grades)


original_student.add_grade(102, 90.5)
original_student.toggle_active_status()
print(original_student.grades)
print(original_student)
original_student.toggle_active_status()
print(original_student)
