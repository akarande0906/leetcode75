class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        leftProd = [1]*n
        rightProd = [1]*n
        output = []
        for num in range(1,n):
            leftProd[num] = leftProd[num - 1] * nums[num - 1]
        for num in range(n-2,-1,-1):
            rightProd[num] = rightProd[num + 1] * nums[num + 1]
        for num in range(n):
            output.append(leftProd[num] * rightProd[num])
        return output

if __name__ == '__main__':
     print(Solution().productExceptSelf([1,2,3,4]))
     print(Solution().productExceptSelf([-1,1,0,-3,3]))

