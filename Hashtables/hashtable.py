class HashTable:

    def __init__(self):
        """Create a new empty map. Returns an empty map collection."""
        self.map = {}

    def put(self, key, val):
        """Add a new key-value pair to the map. If the key is already
        in the map then replace the old value with the new value.
        """
        self.map[key] = val

    def get(self, key):
        """Returns the value stored in the map corresponding to given key.
        Otherwise returns nothing."""
        if key in self.map:
            return self.map[key]

        return None

    def search(self, key):
        """Returns True if key is present in the map. Otherwise returns False """
        if key in self.map:
            return True

        return False

    def replace(self, key, val):
        """Replace a value stored corresponding to the given key in the map with new value."""
        if key in self.map:
            self.map[key] = val

        else:
            return "Key does not found. Value cannot be replaced."

    def print_map(self):
        """Iterates and return the keys and values in the dictionary."""
        for key, value in self.map.items():
                return key, value

    def size(self):
        """Returns the size or length of the key-value pairs stored in the map."""
        return len(self.map)

    def remove(self, key):
        """Deletes the key-value pair from the map."""
        if key in self.map:
            del self.map[key]

        return "No key-value pairs to remove."


