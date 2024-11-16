class SimpleHashTable:
    """A basic hash table implementation using chaining for collision resolution."""

    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair."""
        index = self._hash(key)
        # Check for existing key
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update value if key already exists
                return
        # Add new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        """Retrieve value for given key."""
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        """Delete a key-value pair."""
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                return self.table[index].pop(i)[1]  # Return the deleted value
        return None
