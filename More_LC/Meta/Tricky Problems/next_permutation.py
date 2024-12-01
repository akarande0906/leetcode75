'''
LC 31: Next Permutation
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
For example: the next permutation of arr = [2,3,1] is [3,1,2].
The next permutation of arr = [1,2,3] is [1,3,2].
If we cannot find the next permutation, return the first permutation instead. For example : [3,2,1] => Return [1,2,3]
'''
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Iterate the current permutation from right to left. 
        # Find the first element that is not in increasing order.
        # That is the pivot. Swap this element with the next largest element in the list
        # Then reverse the array to the right of the pivot.
        pivot = -1
        # First find a pivot that is the element that is not decrasing.
        # This will give us the point where we have to swap since all elements after it have reached their max in that subarray
        for index in range(len(nums)-1, 0, -1):
            if nums[index] > nums[index - 1]:
                pivot = index - 1
                break
        # If we dont find a pivot, return the reverse of the array as the array is at the max
        if pivot == -1:
            nums.reverse()
        else:
            # Find the next largest element in the right of the pivot
            # Once we can do we can swap with it as this will be the next permutation starter
            max_elem = float('inf')
            max_id = -1
            for index in range(pivot+1, len(nums)):
                if nums[index] > nums[pivot] and nums[index] <= max_elem:
                    max_elem = nums[index]
                    max_id = index
            nums[pivot], nums[max_id] = nums[max_id], nums[pivot]
            # Now reverse the array to the right of the pivot: [1,3,5,4,2] => [1,3,2,4,5]
            nums[pivot+1::] = nums[pivot+1::][::-1]
        
        