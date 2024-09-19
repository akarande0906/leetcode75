class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the max product, min product, and result with the first element
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            if num < 0:
                # Swap max and min products when encountering a negative number
                max_product, min_product = min_product, max_product
            
            # Update the max and min products
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            # Update the result with the maximum product found so far
            result = max(result, max_product)
        
        return result
        

sol = Solution()
print(sol.maxProduct([2,3,-2,4]))
print(sol.maxProduct([-2,0,-1]))
print(sol.maxProduct([-2,3,-4]))
print(sol.maxProduct([2,3,-2,-4]))
