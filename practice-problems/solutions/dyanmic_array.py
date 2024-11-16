class DynamicArray:
    def __init__(self, initial_size=4):
        self.array = [None] * initial_size
        self.size = initial_size
        self.length = 0

    def append(self, element):
        """Add element to end of array, resize if needed."""
        if self.length == self.size:
            self._resize()
        self.array[self.length] = element
        self.length += 1

    def insert(self, index, element):
        """Insert element at index."""
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if self.length == self.size:
            self._resize()
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.length += 1

    def remove(self, index):
        """Remove element at index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1

    def get(self, index):
        """Get element at index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def _resize(self):
        """Resize array to double its current size."""
        self.size *= 2
        new_array = [None] * self.size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array


# Test cases
def test_dynamic_array():
    arr = DynamicArray()

    # Test 1: Append beyond initial size
    for i in range(6):
        arr.append(i)
    assert arr.size >= 6, "Array should resize"

    # Test 2: Insert in the middle
    arr.insert(2, 10)
    assert arr.get(2) == 10, "Insert failed"

    print("All tests passed!")

# Run the tests
test_dynamic_array()
