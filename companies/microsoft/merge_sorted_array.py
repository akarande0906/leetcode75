'''
Leetcode 88: Merge Sorted Array in place
'''
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Here length of nums1 is enough to contain all elements from nums1 and nums2
        last = m + n - 1 # The last element in the nums1 array
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        while n > 0: # There is no need to do this for m as the lesser items are already in place
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        print (nums1)

merge = Solution().merge
merge([1,2,3,0,0,0], 3, [2,5,6], 3)
merge([1],1,[],0)
merge([0],0,[1],1)
merge([1,2,3,0,0],3,[4,5],2)