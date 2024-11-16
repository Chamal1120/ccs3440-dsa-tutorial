from array_operations import (
    ArrayOperations,
)  # Ensure ArrayOperations is correctly imported


class StudentManagementSystem:
    def __init__(self, capacity):
        self.roster = ArrayOperations(capacity)
        self.id_index = {}  # For quick lookups by ID

    def add_student(self, student):
        # Add to array
        index = self.roster.length
        self.roster.insert(index, student)
        # Add to index
        self.id_index[student["id"]] = index
        print(f"Added student: {student['name']}")

    def find_student_by_id(self, student_id):
        # Use index for O(1) lookup
        if student_id in self.id_index:
            index = self.id_index[student_id]
            return self.roster.access(index)
        return None

    def find_students_by_grade(self, grade):
        # Linear search for all students with matching grade
        matches = []
        for i in range(self.roster.length):
            student = self.roster.access(i)
            if student["grade"] == grade:
                matches.append(student)
        return matches


# Usage example
def run_student_management_example():
    print("\n=== Student Management System Example ===")

    # Initialize system
    sms = StudentManagementSystem(10)

    # Add some students
    students = [
        {"id": "S001", "name": "John Doe", "grade": "A", "major": "CS"},
        {"id": "S002", "name": "Jane Smith", "grade": "B", "major": "Math"},
        {"id": "S003", "name": "Bob Wilson", "grade": "A", "major": "Physics"},
        {"id": "S004", "name": "Alice Brown", "grade": "A", "major": "CS"},
    ]

    for student in students:
        sms.add_student(student)

    # Find student by ID
    print("\nSearching for student S003:")
    student = sms.find_student_by_id("S003")
    if student:
        print(f"Found: {student['name']} - {student['major']}")
    else:
        print("Student not found.")

    # Find all students with grade A
    print("\nSearching for students with grade A:")
    a_students = sms.find_students_by_grade("A")
    for student in a_students:
        print(f"{student['name']} - {student['major']}")


# Run the example
run_student_management_example()
