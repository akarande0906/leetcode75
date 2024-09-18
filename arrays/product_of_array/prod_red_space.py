class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        p = nums[0]
        output = []
        sol = [1] * n
        t = nums[-1]
        for num in range(1,n):
            sol[num] *= p
            p *= nums[num]
        for num in range(n-2,-1,-1):
            sol[num] *= t
            t *= nums[num]
        
        return sol

if __name__ == '__main__':
     print(Solution().productExceptSelf([1,2,3,4]))
     print(Solution().productExceptSelf([-1,1,0,-3,3]))

