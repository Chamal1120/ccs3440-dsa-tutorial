from collections import Counter

def find_duplicates(arr):
    """
    Find all elements that appear more than once in the array.
    """
    counts = Counter(arr)
    return [key for key, value in counts.items() if value > 1]


def find_missing_number(arr, n):
    """
    Find the missing number in an array containing n-1 numbers from 1 to n.
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


# Test cases
def test_search_problems():
    # Test duplicates
    result = find_duplicates([1, 3, 4, 2, 2, 1, 5, 3])
    assert set(result) == {1, 2, 3}, "Duplicate finding failed"

    # Test missing number
    result = find_missing_number([1, 2, 4, 6, 3, 7, 8], n=8)
    assert result == 5, "Missing number finding failed"

    print("All tests passed!")


# Run the tests
test_search_problems()
