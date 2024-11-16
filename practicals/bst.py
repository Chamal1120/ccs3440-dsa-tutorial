class TreeNode:
    """Binary Search Tree Node.

    Attributes:
        data: Node's data
        left: Left child node
        right: Right child node
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation with search and insert operations."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert new node with data into the tree."""
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Recursively find correct position and insert the node."""
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, target_id):
        """Search for node with the target_id."""
        result = self._search_recursive(self.root, target_id)
        comparisons = self._count_comparisons(self.root, target_id)
        return {"found": result is not None, "data": result, "comparisons": comparisons}

    def _search_recursive(self, node, target_id):
        """Recursive search operation."""
        if node is None or node.data["id"] == target_id:
            return node.data if node else None
        if target_id < node.data["id"]:
            return self._search_recursive(node.left, target_id)
        return self._search_recursive(node.right, target_id)

    def _count_comparisons(self, node, target_id, count=0):
        """Count the number of comparisons in search."""
        if node is None:
            return count
        count += 1
        if node.data["id"] == target_id:
            return count
        if target_id < node.data["id"]:
            return self._count_comparisons(node.left, target_id, count)
        return self._count_comparisons(node.right, target_id, count)
