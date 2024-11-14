''' LC: 1151 '''
class Solution:
    def minSwaps(self, data: list[int]) -> int:
        # Find number of 1s
        ones = sum(data)
        # Find sub array with length 'ones' with max number of 1s
        lptr = 0
        ones_in_window = 0
        max_ones = 0
        for rptr in range(len(data)):
            if data[rptr]:
                ones_in_window += 1
                max_ones = max(max_ones, ones_in_window)
            if rptr - lptr + 1 == ones:
                if data[lptr]:
                    ones_in_window -= 1
                lptr += 1
        return ones - max_ones

ms = Solution().minSwaps
print (ms([1,0,1,0,1]))
print (ms([1,0,1,0,1,0,0,1,1,0,1]))
print (ms([0,0,0,1,0]))
