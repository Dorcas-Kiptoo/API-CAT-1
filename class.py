class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students in the classroom.")
        else:
            print("List of students:")
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                avg = student.get_average_grade()
                print(f"Average grade for {student.name} is {avg:.2f}")
                return
        print(f"No student found with the name {student_name}.")

    def get_class_average_for_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades found for subject {subject}.")
            return
        class_average = total / count
        print(f"Class average for {subject} is {class_average:.2f}")

# Demonstration
def main():
    classroom = Classroom()

    # Adding students
    student1 = Student("Alice")
    student1.add_grade("Math", 90)
    student1.add_grade("API", 85)

    student2 = Student("Robert")
    student2.add_grade("Math", 80)
    student2.add_grade("API", 78)

    classroom.add_student(student1)
    classroom.add_student(student2)

    # Display all students
    classroom.display_all_students()

    # Get the average grade of a student
    classroom.get_student_average("Alice")
    classroom.get_student_average("Robert") 

    # Get the class average for a subject
    classroom.get_class_average_for_subject("Math")
    classroom.get_class_average_for_subject("API")

if __name__ == "__main__":
    main()
