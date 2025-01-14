'''
LC 88: Merge Sorted Array
'''
class Solution:
    def mergeSortedArray(self, nums1, m, nums2, n):
        # nums1 has length m + n with m elements for nums1
        # nums2 has length n
        last = m + n - 1
        m -= 1
        n -= 1
        while m > -1 and n > -1:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        #while m >= 0:
        #    nums1[last] = nums1[m]
        #    m -= 1
        #    last -= 1
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
        print (nums1)

sol = Solution().mergeSortedArray
sol([1,2,3,0,0,0], 3, [2,5,6], 3)
sol([1], 1, [], 0)
sol([0], 0, [1], 1)
sol([4,5,6,0,0,0], 3, [1,2,3], 3)
sol([4,5,6,7,0,0,0], 4, [1,2,3], 3)
sol([1,2,3,4,0,0,0], 4, [5,6,7], 3)
