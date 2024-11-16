from searching_algos import binary_search_detailed

def phone_directory_example():
    print("\n=== phone Directory Search Example ===")

    # Sorted phone directory
    contacts = [
        {"name": "Adams, John", "phone": "123-456-7890"},
        {"name": "Brown, Mary", "phone": "234-567-8901"},
        {"name": "Davis, Steve", "phone": "345-678-9012"},
        {"name": "Johnson, Lisa", "phone": "456-789-0123"},
        {"name": "Wilson, Mike", "phone": "567-890-1234"}
    ]

    # Binary search by name
    search_name = "Davis, Steve"
    result = binary_search_detailed(
        contacts,
        search_name,
        key=lambda x: x["name"]
    )

    print(f"\nSearching for contact: {search_name}")
    if result["found"]:
        contact = contacts[result["index"]]
        print(f"Found: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Found in {result['comparisons']} comparisons")
    else:
        print("Contact not found")

# Run example
phone_directory_example()
