class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Can use hash map but set is faster
        seen = set(nums)
        return len(seen) != len(nums)
        

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]))
    print(Solution().containsDuplicate([1,2,3,4]))
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(Solution().containsDuplicate([1,2,3,4,5,6,7,8,9,1]))
