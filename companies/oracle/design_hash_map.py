'''
LC 764: Design Hash Map
'''
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key: int) -> int:
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]: 
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

class MyHashMap:

    def __init__(self):
        self.key_space = 2069 # Prime number to reduce collisions
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        # Get the bucket with the key
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1)) # Should return 1
print(obj.get(3)) # Should return -1
obj.put(2,1)
print(obj.get(2)) # Should return 1
obj.remove(2)
print(obj.get(2)) # Should return -1