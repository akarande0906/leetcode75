'''
LC 1539: Kth missing positive number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
'''
class Solution:
    '''' O(n) TC 
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_count = 0
        cur_min = 0
        for i in range(len(arr)):
            if arr[i] - cur_min > 1:
                missing_count += arr[i] - cur_min - 1
                if missing_count >= k:
                    # Find the missing number
                    return arr[i] - (missing_count - k) - 1
            cur_min = arr[i]
        return arr[i] + (k - missing_count) 
    '''

    def findKthPositive(self, arr: list[int], k: int) -> int:
        '''
        Comparing a consecutive array with one with gaps
        [2,3,4,7,11] => [1,2,3,4,5], we can see that a number at 
        index 0: number of missing elements is 2 - 1 = 1
        index 3: number of missing elements is 7 - 4 = 3 
        that is num[idx] - idx - 1
        ''' 
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else: # More than k diffs already
                right = pivot - 1
        #print (left)
        return left + k
        




findKthNum = Solution().findKthPositive
print(findKthNum([2,3,4,7,11], 8))
print(findKthNum([1,2,3,4], 2))
print(findKthNum([1,3,5,7], 3))