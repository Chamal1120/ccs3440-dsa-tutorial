class Node:
    """A single node in the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List implementation with search capabilities."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node at the end (O(n))."""
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insert_front(self, data):
        """Add a new node at the beginning (O(1))."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete first occurrence of data (O(n))."""
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def linear_search(self, target):
        """Search for an element and return its position."""
        current = self.head
        position = 0
        while current:
            if current.data == target:
                return {"position": position, "found": True, "data": current.data}
            current = current.next
            position += 1
        return {"position": -1, "found": False, "data": None}

    def display(self):
        """Return list of all elements."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
