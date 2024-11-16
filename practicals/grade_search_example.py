from searching_algos import binary_search_detailed

def grade_search_example():
    print("\n=== Student Grade Search Example ===")

    # Sorted student grades
    students = [
        {"id": "S001", "name": "Alice", "grade": 75},
        {"id": "S002", "name": "Bob", "grade": 82},
        {"id": "S003", "name": "Charlie", "grade": 88},
        {"id": "S004", "name": "David", "grade": 92},
        {"id": "S005", "name": "Eve", "grade": 95},
    ]

    # Binary search for grade
    target_grade = 88
    result = binary_search_detailed(students, target_grade, key=lambda x: x["grade"])

    print(f"\nSearching for grade: {target_grade}")
    if result["found"]:
        student = students[result["index"]]
        print(f" Found student: {student['name']}")
        print("\nSearch steps:")
        for i, step in enumerate(result["steps"], 1):
            print(f"Step {i}")
            print(f"checking range: {step['left']} to {step['right']}")
            print(f"Middle element: {step['mid']}")
            print(f"Action: {step['action']}")
            print(f"Action: {step['action']}")
    else:
        print("Grade not found")

# Run the example
grade_search_example()
