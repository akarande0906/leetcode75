'''
Given two integers N and K, the task is to find the string S of minimum length to contain all possible strings of size N as a substring. The characters of the string should be from integers ranging from 0 to K-1. 

Input: N = 2, K = 2
Output: 00110
Explanation: Allowed characters are from 0 to k-1 (i.e., 0 and 1). There are 4 string possible of size N=2 (i.e “00”, “01”,”10″,”11″) “00110” contains all possible string as a substring. It also has the minimum length.


Input: N = 2, K = 3
Output: 0010211220
Explanation: Allowed characters are from 0 to k-1 (i.e., 0, 1 and 2). There are total 9 strings possible of size N, given output string has the minimum length that contains all those strings as substring.

'''


class Solution:
    def findString(self, n, k):
        ans = '0'
        visited = set()
        k -= 1 # 0 based indexing
        # First initialize string :
        ans = '0' * n
        visited.add(ans)

        while (len(visited) < pow((k+1), n)):
            previous = ans[-n+1:]
            for cntr in range(k, -1, -1): # Start with the max value
                if previous + str(cntr) in visited:
                    continue
                else:
                    ans += str(cntr)
                    visited.add(previous + str(cntr))
                    break
        return ans

    def findString2(self, n, k):
        ans = "0"
        k -= 1
        visited = set()
        visited.add("0")

        while len(visited) < pow((k + 1), n):
            previous = ans[-n + 1:]
            for i in range(k, -1, -1):
                currStr = previous + str(i)
                if currStr not in visited:
                    visited.add(currStr)
                    ans += str(i)
                    break

        return ans


print (Solution().findString(2, 2))
#print (Solution().findString2(2, 2))
print (Solution().findString(2, 3))
#print (Solution().findString2(2, 3))
print (Solution().findString(3, 3))
#print (Solution().findString2(3, 3))

