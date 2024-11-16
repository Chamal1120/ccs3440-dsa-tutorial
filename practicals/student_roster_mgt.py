from array_operations import ArrayOperations

def student_roster_example():
    print("\n=== Student Roster Example ===")
    roster = ArrayOperations(20)

    # Sample student data
    students = [
        {"id": "S001", "name": "John", "grade": "A"},
        {"id": "S002", "name": "Emma", "grade": "B"},
        {"id": "S003", "name": "Michael", "grade": "A-"}
    ]

    # Add initial students
    print("Adding students to roster:")
    for i, student in enumerate(students):
        roster.insert(i, student)
        print(f"Added {student['name']} ID: {student['id']}, Grade: {student['grade']}")

    # show current roster
    print("\nCurrent roster:")
    for student in roster.display():
        print(f"{student['name']}: {student['grade']}")

    # Add new student in middle
    new_student = {"id": "S004", "name": "Sarah", "grade": "B+"}
    print(f"\nAdding new student {new_student['name']} at position 1")
    roster.insert(1, new_student)

    print("\nUpdated roster:")
    for student in roster.display():
        print(f"{student['name']}: {student['grade']}")

# Run Example
student_roster_example()
