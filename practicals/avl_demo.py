from avl_tree import BalancedBST


def demonstrate_balanced_bst():
    print("\n=== Balanced BST Demonstration ===")
    tree = BalancedBST()

    # Sample student data
    students = [
        {"id": 5, "name": "Alice", "grade": 95},
        {"id": 3, "name": "Bob", "grade": 88},
        {"id": 7, "name": "Charlie", "grade": 92},
        {"id": 1, "name": "David", "grade": 85},
        {"id": 9, "name": "Eve", "grade": 98},
        {"id": 4, "name": "Frank", "grade": 87},
        {"id": 6, "name": "Grace", "grade": 93},
    ]

    # Insert students
    print("Inserting students...")
    for student in students:
        tree.insert(student)
        print(f"Added: {student['name']} (ID: {student['id']})")

    # Demonstrate different traversals
    print("\nTraversal Demonstrations:")

    print("\nInorder Traversal (sorted by ID):")
    for student in tree.inorder():
        print(f"{student['name']}: {student['id']}")

    print("\nLevel Order Traversal (by tree level):")
    for student in tree.level_order():
        print(f"{student['name']}: {student['id']}")

    # Search demonstration
    print("\nSearch Demonstrations:")
    search_ids = [4, 8]  # One existing, one non-existing
    for search_id in search_ids:
        result = tree.search(search_id)
        print(f"\nSearching for ID: {search_id}")
        if result["found"]:
            print(f"Found: {result['data']['name']}")
        else:
            print("Student not found")
        print(f"Search path: {' -> '.join(map(str, result['path']))}")


# Run demonstration
def main():
    demonstrate_balanced_bst()


if __name__ == "__main__":
    main()
