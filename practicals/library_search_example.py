from searching_algos import linear_search_detailed

def library_search_example():
    print("\n=== Library Book Search Example ===")

    # Book database
    books = [
            {"id": "B001", "title": "Python Programming", "author": "John Smith"},
            {"id": "B002", "title": "Data Structures", "author": "Jane Doe"},
            {"id": "B003", "title": "Algorithms", "author": "Alan Johnson"},
            {"id": "B004", "title": "Web Development", "author": "Sarah Wilson"},
            {"id": "B005", "title": "Machine learning", "author": "Mike Brown"}
    ]

    # Linear search for a book by ID
    search_id = "B003"
    result = linear_search_detailed(books, search_id, key=lambda book: book["id"])

    print(f"\nSearching for book ID: {search_id}")
    if result["found"]:
        book = books[result["index"]]
        print(f"found: {book['title']} by {book['author']}")
        print(f"Comparisons made: {result['comparisons']}")
    else:
        print("Book not found")

library_search_example()
