
import json
from abc import (
    ABC, abstractmethod
    )

class Person(ABC):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    @abstractmethod
    def get_details(self):
        pass
    
    
class Teacher(Person):
    def __init__(self, name, surname, age, subject):
        super().__init__(name, surname, age)
        self.subject = subject
        self.email = f'{name.lower()}.{surname.lower()}@gmail.com'
    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "email": self.email,
            "subject": self.subject
            }
    
    
class Student(Person):
    student_id=0
    
    def __init__(self, name, surname, age):
        super().__init__(name,surname,age)
        self.email = f'{name.lower()}.{surname.lower()}@gmail.com'
        Student.student_id += 1
        self.student_id = f"ID - {Student.student_id}"
        
    def get_details(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "email": self.email,
            "student_id": self.student_id
            }   
           
            
class Course:
        def __init__(self, title, description, teacher):
            self.title = title
            self.description = description
            self.teacher = teacher
            self.students=[]
            
        def add_student(self, student:Student):
            self.students.append(student)
        
        def get_details(self):
            return{
                "title":self.title,
                "description":self.description,
                "teacher":self.teacher.get_details(),
                "students": [student.get_details() for student in self.students]
            }
         
            
class OnlinePlatform:
    def __init__(self):
        self.courses=[]
        self.people=[]
        
    def add_course(self,course:Course):
        self.courses.append(course)
    
    def add_people(self,people):
        self.people.append(people)
    
    def all_course(self):
        for course in self.courses:
            return(course.get_details())
            
    def all_people(self):
        return [student.get_details() for student in self.people] 

    def save_to_json_course(self,filename):
        data={
        "courses":self.all_course()
            }
        with open(filename,'w') as f:
            json.dump(data,f,indent=4)
    
    def save_to_json_people(self,filename):
        data={
            "people":self.all_people()
            }
        with open(filename,'w') as f:
            json.dump(data,f,indent=4)
    
teacher=Teacher('Adil', 'Yusublu', 22, 'Programming')

student1=Student('Konul', 'Huseynli', 21)
student2=Student('Gunay', 'Memmedov', 23)
student3=Student('Aysun', 'Qasimli', 25)
student4=Student('Emil', 'Humbetov', 34)
student5=Student('Ali', 'Aliyev', 17)

course=Course('OOP', "You will learn oop's principals",teacher)
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.add_student(student4)
course.add_student(student5)

print(course.get_details())


platform=OnlinePlatform()
platform.add_course(course)
platform.add_people(teacher)
platform.add_people(student1)
platform.add_people(student2)
platform.add_people(student3)
platform.add_people(student4)

platform.all_course()
platform.all_people()
platform.save_to_json_course('exam2_consoleproject\data.json')
platform.save_to_json_people('exam2_consoleproject\data2.json')
