class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Konrad Różański", [60, 75, 80, 90, 65])
student2 = Student("Wojciech Piasecki", [40, 35, 55, 48, 42])

# Sprawdzenie, czy studenci zaliczyli
print(f"{student1.name} zdał: {student1.is_passed()}")
print(f"{student2.name} zdał: {student2.is_passed()}")
