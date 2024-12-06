'''
LC 380: Insert Delete Get Ramdon O(1)
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
import random
### To implement O(1) on average, we need a hash map in addition to a list
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.dict:
            return False
        index = self.dict[val]
        if index != len(self.dict) - 1:
            last_elem = self.list[-1]
            self.list[index], self.dict[last_elem] = self.list[len(self.dict) - 1], index
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()