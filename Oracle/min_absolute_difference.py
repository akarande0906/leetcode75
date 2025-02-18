'''
LC 1200: Minimum Absolute Difference
'''
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # First Sort the array
        arr.sort()

        # now compare each pair of elements 
        # if the diff is equal to the current min diff, 
        # append to the array
        # if the diff is lesser than the current min diff,
        # Reset the current min diff and array
        min_diff = float('inf')
        output_arr = []
        for a in range(0, len(arr) - 1):
            cur_diff = abs(arr[a] - arr[a+1])
            if cur_diff < min_diff:
                min_diff = cur_diff
                output_arr = [[arr[a], arr[a+1]]]
            elif cur_diff == min_diff:
                output_arr.append([arr[a], arr[a+1]])
        return output_arr
    # Time: O(nlogn)
    # Space: O(n)
min_diff = Solution().minimumAbsDifference
assert min_diff([4,2,1,3]) == [[1,2],[2,3],[3,4]]
assert min_diff([1,3,6,10,15]) == [[1,3]]
assert min_diff([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]


# Alternate Solution : Counting Sort 
""" 
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Counting Sort

        # Find the min and max elements in the array
        min_val = float('inf')
        max_val = float('-inf')
        for i in range(len(arr)):
            min_val = min(arr[i], min_val)
            max_val = max(arr[i], max_val)
        # Create an array where we map the elements 
        # Mark elements matching the value to 1
        num_line_array = [0] * (max_val - min_val + 1)
        for cur_val in arr:
            num_line_array[cur_val - min_val] = 1
        ret_arr = []
        max_diff = float('inf')
        prev_val = min_val
        for i in range(1, len(num_line_array)):
            cur_val = i + min_val
            if num_line_array[i] == 1:
                cur_diff = abs(cur_val - prev_val)
                if cur_diff == max_diff:
                    ret_arr.append([prev_val, cur_val])
                elif cur_diff < max_diff:
                    max_diff = cur_diff
                    ret_arr = [[prev_val, cur_val]]
                prev_val = cur_val
        return ret_arr 
"""
# Time: O(M+N) where M is the range of the array and N is the length of the array
# Space: O(M+N) where M is the range of the array and N is the length of the array


