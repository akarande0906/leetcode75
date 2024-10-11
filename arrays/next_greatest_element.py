'''
496. Next Greater Element I
'''
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ret_arr = []
        n2_map = {}
        stack = []
        for i in nums2[::-1]:
            while stack:
                if stack[-1] > i:
                    n2_map[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop()
            if not stack:
                n2_map[i] = -1
                stack.append(i)
        for j in nums1:
            ret_arr.append(n2_map[j])
        return ret_arr
        

sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
print(sol.nextGreaterElement([2,4], [1,2,3,4]))
print(sol.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
