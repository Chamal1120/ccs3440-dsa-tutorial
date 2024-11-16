from array_operations import ArrayOperations

def shopping_cart_example():
    """ Use arrayOperations to simulate a shopping cart example"""
    print("\n=== Shopping Cart Example ===")
    # Initialize cart with size 10
    cart = ArrayOperations(10)

    items = [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Mouse", "price": 29.99},
            {"id": 3, "name": "Keyboard", "price": 59.99}
    ]

    # Demonstrate insert operation
    print("Adding items to cart:")
    for i, item in enumerate(items):
        cart.insert(i, item)
        print(f"Added {item['name']} - ${item['price']}")

    print("\nCurrent cart contents:")
    print(cart.display())

    # Demonstrate delete operation
    print("\nRemoving second item (Mouse)...")
    cart.delete(1)
    print("Update cart contents:")
    print(cart.display())

    # Demonstrate access operation
    first_item = cart.access(0)
    print(f"\nFirst item in cart: {first_item['name']} - ${first_item['price']}")

# Execute the example
shopping_cart_example()
