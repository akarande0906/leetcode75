class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        # No need to explicitly reverse. Just need to check if the elements match
        int_map = {}
        for i in range(len(target)):
            int_map[target[i]] = int_map.get(target[i], 0) + 1
        for i in range(len(arr)):
            if not arr[i] in int_map:
                return False
            int_map[arr[i]] = int_map.get(arr[i]) - 1
            if int_map[arr[i]] == 0:
                del int_map[arr[i]]
        return not int_map

print (Solution().canBeEqual([1,2,3,4], [2,4,1,3]))
print (Solution().canBeEqual([7], [7]))
print (Solution().canBeEqual([3,7,9], [3,7,11]))
