class ArrayOperations:
    """ Instantiate a class for array operations"""
    def __init__(self, size):
        """Initialize the array with a fixed size."""
        self.size = size
        self.array = [None] * size
        self.length = 0

    def access(self, index):
        """Return the element at the given index, if within bounds."""
        if 0 <= index < self.length:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def insert(self, index, element):
        """Insert an element at the specified index, shifting as needed."""
        if self.length >= self.size:
            raise OverflowError("Array is full")
        if not 0 <= index <= self.length:
            raise IndexError("Index out of bounds")

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = element
        self.length += 1

    def delete(self, index):
        """Delete the element at the specified index, shifting as needed."""
        if not 0 <= index < self.length:
            raise IndexError("Index out of bounds")

        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.length - 1] = None
        self.length -= 1

    def display(self):
        """Return the current elements in the array."""
        return [self.array[i] for i in range(self.length)]
