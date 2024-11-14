'''
LC 4
'''
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        mid_pt = total // 2
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = mid_pt - i - 2
            n1left = nums1[i] if i >= 0 else float('-infinity')
            n1right = nums1[i+1] if (i + 1) < len(nums1) else float('infinity')
            n2left = nums2[j] if j >= 0 else float('-infinity')
            n2right = nums2[j+1] if (j + 1) < len (nums2) else float('infinity')

            if n1left <= n2right and n2left <= n1right: # Correct partition
                if total % 2: # Odd number of elements
                    return min(n1right, n2right)
                else:
                    return (max(n1left, n2left) + min (n1right, n2right)) / 2
            else:
                if n1left > n2right:
                    r = i - 1
                else:
                    l = i + 1

print (Solution().findMedianSortedArrays([1,3], [2]))
print (Solution().findMedianSortedArrays([1,2], [3,4]))
print (Solution().findMedianSortedArrays([1,2,3,4,5], [3,4,5]))
