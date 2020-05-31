

class Person():
    def __init__(self, name:str, DOB:int):
        self.__name = name
        self.__DOB = DOB
        self.abe = None
    def get_name(self):
        return self.__name

    def get_DOB(self):
        return self.__DOB

    def set_name(self,new_name):
        if(self.__has_any_number(new_name)):
            print("Sorry Name cant have number")
            return
        self.__name = new_name
    def __has_any_number(self,string):
        return "0" in string
    def get_summary(self):
        pass
        # return f"Name: {self.__name}, DOB: {self.__DOB}"

class Student(Person):
    def __init__(self, name: str, DOB: int, email_id:str, student_id:int ):
        super().__init__(name, DOB)
        self.id = student_id
        self.Email = email_id

    def get_summary(self):
        return f"Name: {self.get_name()} Email:{self.Email} Brirth: {self.get_DOB()}"

    def __str__(self):
        return f"Name: {self.get_name()} Email:{self.Email} Brirth: {self.get_DOB()}"

class Teacher(Person):
    def __init__(self, name: str, DOB: int, department:str):
        super().__init__(name, DOB)
    def get_summary(self):
        return f"{self.get_name()} is a Teacher"

new_person_list=[
    Person('Xul', 1990),
    Student('Rafi', 1990, 'some@gmail.com',12),
    Teacher('Aasiw',1222, 'cse')

]

for p in new_person_list:
    print(p.get_summary())

# student = Student('A', 200, 'some@gmail.com',112312)
# print(student.get_summary())
# print(student)
# a_person = Person("rafi",1198)
# print(a_person.get_summary())
# print(a_person.set_name("Rabiul Alam"))
# print(a_person.get_summary())
# print(a_person.DOB)
# a_person.set_name("0Rafi")
# print(a_person.get_summary())

# person_list = [Person("Rafi", 1998), Person("Rafiq", 1997), Person("Rafia", 1999), Person("Rafiuy", 1990)]
#
# for person in person_list:
#     if person.get_DOB() >= 1998:
#         print(person.get_summary())