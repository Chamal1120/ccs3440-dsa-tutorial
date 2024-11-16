def linear_search_detailed(array, target, key=lambda x: x):
    """Detailed linear search implementation"""
    comparisons = 0

    for index, item in enumerate(array):
        comparisons += 1
        current_value = key(item)

        if current_value == target:
            return {
                "index": index,
                "comparisons": comparisons,
                "found": True,
                "search_path": list(range(index + 1)),
            }

    return {
        "index": -1,
        "comparisons": comparisons,
        "found": False,
        "search_path": list(range(len(array))),
    }

def binary_search_detailed(array, target, key=lambda x: x):
    """Detailed binary search implementation"""
    left = 0
    right = len(array) - 1
    comparisons = 0
    steps = []

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        current_value = key(array[mid])

        steps.append(
            {
                "left": left,
                "right": right,
                "mid": mid,
                "current_value": current_value,
                "action": "comparisons",
            }
        )

        if current_value == target:
            steps[-1]["action"] = "found"
            return {
                "index": mid,
                "comparisons": comparisons,
                "steps": steps,
                "found": True,
            }
        if current_value < target:
            steps[-1]["action"] = "move_right"
            left = mid + 1
        else:
            steps[-1]["action"] = "move_left"
            left = mid - 1

    return {
            "index": -1,
            "comparisons": comparisons,
            "steps": steps,
            "found": False
    }
