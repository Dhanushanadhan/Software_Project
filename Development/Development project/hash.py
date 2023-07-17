class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for existing_key, existing_value in bucket:
            if existing_key == key:
                return existing_value
        raise KeyError(f"Key '{key}' not found in the hash table.")



# Retrieve values from the hash table using keys
#print(hash_table.get('Assignment submission'))  # Output: High
#print(hash_table.get('Lab-related queries'))  # Output: Low




