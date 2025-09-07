class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        # No need to explicitly reverse. Just need to check if the elements match
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True

print (Solution().canBeEqual([1,2,3,4], [2,4,1,3]))
print (Solution().canBeEqual([7], [7]))
print (Solution().canBeEqual([3,7,9], [3,7,11]))
