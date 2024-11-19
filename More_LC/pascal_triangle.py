'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it:
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1 
   1 5 10 10 5 1
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        final_arr = [[1]]
        if numRows == 1:
            return final_arr
        factor = 1
        cur_arr = [1] * numRows
        for i in range (1, numRows):
            temp_arr = [1] * (i + 1)
            for j in range (1, i//2 + 1):
                temp_arr[j] = cur_arr[j] + cur_arr[j-1]
                temp_arr[i-j] = temp_arr[j]
            cur_arr[0:i] = temp_arr
            print(temp_arr)
            print(cur_arr)
            final_arr.append(temp_arr)
        return (final_arr)
    
print(Solution().generate(6))