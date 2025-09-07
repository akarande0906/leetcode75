'''
78: Subsets of Array
Given an integer array nums of unique elements, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.output = []
        self.n, self.k = len(nums), None

        def backtrack(first, curr, nums):
            if len(curr) == self.k:
                self.output.append(curr[:]) # Appends a copy
                # print (self.output)
                return
            for i in range(first, self.n):
                curr.append(nums[i])
                backtrack(i+1, curr, nums)
                curr.pop()
        # Each time see how many rows to generate
        for self.k in range(self.n+1):
            backtrack(0, [], nums)
        return self.output
    '''
    TC: O(N * 2^N)) -> We run this n times and generate 2^N possible choices
    SC: O(N) because we append max of n elements in the curr array
    '''
print(Solution().subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]