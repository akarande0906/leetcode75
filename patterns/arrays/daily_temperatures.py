'''
739. Daily Temperatures
'''
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ret_arr = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)-1, -1, -1):
            while stack:
                d, val = stack[-1]
                if val > temperatures[i]:
                    ret_arr[i] = d - i
                    stack.append([i, temperatures[i]])
                    break
                else:
                    stack.pop()
            if not stack:
                ret_arr[i] = 0
                stack.append([i, temperatures[i]])
        return ret_arr


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(sol.dailyTemperatures([30,40,50,60]))
print(sol.dailyTemperatures([30,60,90]))
