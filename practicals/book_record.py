from linked_list import LinkedList

class Book:
    """Book record for library management."""

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __eq__(self, other):
        """Enable comparison with ISBN string."""
        if isinstance(other, str):
            return self.isbn == other
        return False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


def demonstrate_library_linked_list():
    print("\n=== Library Book Management Example ===")
    # Create Library catalog
    catalog = LinkedList()
    # Add sample books
    books = [
        Book("978-0001", "Python Basics", "John Smith"),
        Book("978-0002", "Data Structures", "Jane Doe"),
        Book("978-0003", "Algorithms", "Bob Wilson"),
    ]
    print("Adding books to catalog:")
    for book in books:
        catalog.append(book)
        print(f"Added: {book}")

    # Search for a book
    print("\nSearching for ISBN: 978-0002")
    result = catalog.linear_search("978-0002")
    if result["found"]:
        book = result["data"]
        print(f"Found at position {result['position']}: {book}")
    else:
        print("Book not found")

    # Delete a book
    print("\nDeleting book with ISBN: 978-0001")
    catalog.delete("978-0001")

    # Display updated catalog
    print("\nUpdated catalog:")
    for book in catalog.display():
        print(book)


# Run the example
demonstrate_library_linked_list()
