class TreeNode:
    """Enhanced Binary Search Tree Node with height for AVL balancing"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height used for AVL balancing


class BalancedBST:
    """Self-balancing Binary Search Tree (AVL Tree) implementation with traversal methods"""

    def __init__(self):
        self.root = None

    def _get_height(self, node):
        """Get height of node"""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """Get balance factor of node"""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_height(self, node):
        """Update height of node"""
        if not node:
            return
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _right_rotate(self, y):
        """Right rotation for balancing"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def _left_rotate(self, x):
        """Left rotation for balancing"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, data):
        """Insert new node and maintain balance"""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Recursive insert with balancing"""
        # Standard BST insert
        if not node:
            return TreeNode(data)

        if data["id"] < node.data["id"]:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)

        # Update height
        self._update_height(node)

        # Get balance factor
        balance = self._get_balance(node)

        # Balance the tree if needed
        # Left Left Case
        if balance > 1 and data["id"] < node.left.data["id"]:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and data["id"] > node.right.data["id"]:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and data["id"] > node.left.data["id"]:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and data["id"] < node.right.data["id"]:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Traversal Methods

    def inorder(self):
        """Inorder traversal: left -> root -> right"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        """Preorder traversal: root -> left -> right"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        """Postorder traversal: left -> right -> root"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def level_order(self):
        """Level order (breadth-first) traversal"""
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def search(self, target_id):
        """Search with path tracking"""
        path = []
        result = self._search_recursive(self.root, target_id, path)
        return {"found": result is not None, "data": result, "path": path}

    def _search_recursive(self, node, target_id, path):
        if not node:
            return None
        path.append(node.data["id"])
        if node.data["id"] == target_id:
            return node.data
        if target_id < node.data["id"]:
            return self._search_recursive(node.left, target_id, path)
        return self._search_recursive(node.right, target_id, path)
