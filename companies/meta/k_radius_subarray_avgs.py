'''
LC 2090: K Radius Subarray Averages
You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i with the radius k 
is the average of all elements in nums between the indices i - k and i + k (inclusive). 
If there are less than k elements before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3 Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Input: nums = [100000], k = 0 Output: [100000]
'''
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        cur_sum = 0
        prefix_sums = [0] # Initialize with 0 as the base prefix sum
        max_id = len(nums)
        avgs = [-1] * max_id # Initialize -1s in the averages array
        # Compute the prefix sums
        for num in nums:
            cur_sum += num
            prefix_sums.append(cur_sum)
        # We dont need to run the loop for values < i - k or > i + k as these are already -1
        for i in range(k + 1, max_id - k + 1):
            avgs[i-1] = (prefix_sums[i+k] - prefix_sums[i-k-1])//(2*k+1)
        return avgs

avg = Solution().getAverages
print (avg([7,4,3,9,1,8,5,2,6], 3))
print (avg([100000], 0))
print (avg([8], 10000))
                
