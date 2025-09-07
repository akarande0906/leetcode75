class Solution:
    def findIndexOfSubArraySum(self, arr: list[int], target: int) -> list[int]:
        prefarr = {}
        sum = 0
        for val in range(len(arr)):
            if arr[val] == 0:
                prefarr[0] = val + 1
                continue
            sum += arr[val]
            if sum == target:
                return [1, val + 1]
            prefarr[sum] = val + 1
        #print (prefarr)
        for key, val in prefarr.items():
            if  key < target or key == 0: 
                continue
            if key - target in prefarr:
                return [prefarr[key-target] + 1, val]
        return [-1, -1]


print (Solution().findIndexOfSubArraySum([1,2,3,4,5,6,7,8,9,10], 15))
print (Solution().findIndexOfSubArraySum([1,2,3,7,5], 12))
print (Solution().findIndexOfSubArraySum([1,2,3,0,7,5], 12))
print (Solution().findIndexOfSubArraySum([7,2,15], 2))



