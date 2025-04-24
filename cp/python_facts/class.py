class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):  # Special method to return a string representation
          
        return f"Student(Name: {self.name}, Age: {self.age}, Grade: {self.grade})"
    def display_info(self):
        return f"Name : {self.name} Age : {self.age} and Finally His /Him Grade : {self.grade}"
    


studet1 = Student("Nuredin ", 23, 3.6)
print(studet1)