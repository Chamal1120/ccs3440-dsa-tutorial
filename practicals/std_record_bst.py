from bst import BinarySearchTree

def demonstrate_student_bst():
    print("\n=== Student Record System Using BST ===")

    # Create BST
    student_tree = BinarySearchTree()

    # Add sample students
    students = [
        {"id": 101, "name": "Alice", "grade": 95},
        {"id": 103, "name": "Bob", "grade": 88},
        {"id": 102, "name": "Charlie", "grade": 92},
        {"id": 105, "name": "David", "grade": 85},
        {"id": 104, "name": "Eve", "grade": 90},
    ]

    print("Adding students to BST:")
    for student in students:
        student_tree.insert(student)
        print(f"Added: {student['name']} (ID: {student['id']})")

    # Search demonstrations
    test_ids = [102, 106]  # One existing, one non-existing
    for student_id in test_ids:
        print(f"\nSearching for student ID: {student_id}")
        result = student_tree.search(student_id)
        if result["found"]:
            student = result["data"]
            print(f"Found: {student['name']} - Grade: {student['grade']}")
        else:
            print("Student not found.")
        print(f"Number of comparisons: {result['comparisons']}")


# Run the demonstration
demonstrate_student_bst()
