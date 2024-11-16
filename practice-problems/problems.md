### Problem 1: Custom Array Implementation
Implement a dynamic array that automatically resizes when full.

```python
class DynamicArray:
    def __init__(self, initial_size=4):
        self.array = [None] * initial_size
        self.size = initial_size
        self.length = 0

    # TODO: Implement these methods
    def append(self, element):
        """Add element to end of array, resize if needed"""
        pass

    def insert(self, index, element):
        """Insert element at index"""
        pass

    def remove(self, index):
        """Remove element at index"""
        pass

    def get(self, index):
        """Get element at index"""
        pass


# Test cases
def test_dynamic_array():
    arr = DynamicArray()

    # Test 1: Append beyond initial size
    for i in range(6):
        arr.append(i)
    assert arr.size >= 6, "Array should resize"

    # Test 2: Insert in middle
    arr.insert(2, 10)
    assert arr.get(2) == 10, "Insert failed"
```

### Problem 2: Array Search Problems
Implement different search scenarios.

```python
def find_duplicates(arr):
    """
    Find all elements that appear more than once in the array.
    Example:
    Input: [1, 3, 4, 2, 2, 1, 5, 3]
    Output: [1, 2, 3]
    """
    pass

def find_missing_number(arr):
    """
    Find the missing number in an array containing n-1 numbers from 1 to n.
    Example:
    Input: [1, 2, 4, 6, 3, 7, 8], n=8
    Output: 5
    """
    pass


# Test cases
def test_search_problems():
    # Test duplicates
    result = find_duplicates([1, 3, 4, 2, 2, 1, 5, 3])
    assert set(result) == {1, 2, 3}, "Duplicate finding failed"

    # Test missing number
    result = find_missing_number([1, 2, 4, 6, 3, 7, 8])
    assert result == 5, "Missing number finding failed"
```

