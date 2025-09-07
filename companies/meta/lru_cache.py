'''
LC 146: LRU Cache
Design an LRU Cache such that get and put return in O(1) time
'''

class DLL:
    def __init__(self, key = None, val = None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    
    def __init__(self, capacity: int):
        # Define a doubly linked list 
        # To store the cache. This is needed so 
        # we can efficiently access both ends
        # Head and tail are dummy nodes 
        # that make adds/removes easier
        self.head = DLL()
        self.tail = DLL()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache_map = {}
        self.capacity = capacity

    
    def _remove_(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        # We need to check if key is present first
        if not key in self.cache_map:
            return -1
        node = self.cache_map[key]
        self._remove_(node)
        self._add_(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            old_node = self.cache_map[key]
            self._remove_(old_node)
        if len(self.cache_map) == self.capacity:
            # We need to evict least recently used
            node = self.head.next
            self._remove_(node)
            del self.cache_map[node.key]
        new_tail = DLL(key, value)
        self.cache_map[key] = new_tail
        self._add_(new_tail)

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))

# Time Complexity: O(1) for both get and put
