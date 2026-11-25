# Unit 1 - Q1: Student Management System (OOP)

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        return "F"

    def __str__(self):
        return (f"Roll No: {self.roll_number} | Name: {self.name} | "
                f"Marks: {self.marks} | Grade: {self.get_grade()}")


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the college.")
            return
        print("\n--- Student Details ---")
        for s in self.students:
            print(s)


def main():
    college = College()
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nStudent {i + 1}:")
        roll = input("Roll Number: ")
        name = input("Name: ")
        marks = float(input("Marks: "))
        college.add_student(Student(roll, name, marks))
    college.display_students()


if __name__ == "__main__":
    main()
