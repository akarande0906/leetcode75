class Solution:
    def minSwaps(self, data: list[int]) -> int:
        count = 0
        onesCount = data.count(1) # Or onesCount = sum(data)
        if onesCount == 1:
            return 0
        left , right, curr = 0, 0, 0
        while right < len(data):
            if data[right] == 1:
                curr += 1
            count = max(curr, count)
            print('Values: {} {} {}'.format(curr, left, right))
            right += 1
            if right - left + 1 > onesCount:
                if data[left] == 1:
                    curr -= 1
                left += 1
        return onesCount - count


print (Solution().minSwaps([1,0,1,0,1]))
print (Solution().minSwaps([1,0,0,1,0,0,1]))
print (Solution().minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
            

