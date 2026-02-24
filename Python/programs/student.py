class Student:
    def __init__(self, name, age, student_id, percentage):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.percentage = percentage
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Percentage: {self.percentage}%")

student1 = Student("Alice", 20, "S12345", 88.5)
student1.display_details()

student2 = Student("Bob", 22, "S67890", 92.0)
student2.display_details()

student3 = Student("Charlie", 19, "S54321", 76.5)

student3.display_details()

class Grad_Student(Student):
    def __init__(self, name, age, student_id, percentage, stream):
        super().__init__(name, age, student_id, percentage)
        self.stream = stream

    def display_details(self):
        super().display_details()
        print(f"Stream: {self.stream}") 

grad_student1 = Grad_Student("David", 24, "G11223", 85.0, "Computer Science")
grad_student1.display_details()

grad_student2 = Grad_Student("Eva", 23, "G44556", 90.5, "Mathematics")
grad_student2.display_details()

