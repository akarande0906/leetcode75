'''
LC 189: Rotate Array 
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp_arr = nums[len(nums) - k:]
        for i in range(len(nums) - 1, k-1, -1):
            nums[i] = nums[i-k]
        nums[0:k] = temp_arr
        print(nums)

    # TC : O(n)
    # SC : O(k)

    def rotate_v2(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # First reverse array
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)  
        print(nums)
    


rotate = Solution().rotate_v2
rotate([1,2,3,4,5,6,7], 3)
rotate([-1,-100,3,99], 2)
rotate([1,2,3,4,5,6,7], 3)
rotate([1,2], 3)