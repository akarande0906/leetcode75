'''
LC 1652: Diffuse the Bomb
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
'''
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        decode_arr = [0] * n
        if k == 0:
            return decode_arr
        for i in range(n):
            sum = 0
            if k < 0:
                for j in range(1,abs(k)+1):
                    id = i - j
                    if id < 0:
                        id = n + id
                    sum += code[id]
            else:
                for j in range(1,k+1):
                    id = i + j
                    if id >= n:
                        id = id - n
                    sum += code[id]
            decode_arr[i] = sum
        return decode_arr
    
'''
Alternately using sliding window 
'''
    
print (Solution().decrypt([5,7,1,4], 3))
print (Solution().decrypt([1,2,3,4], 0))
print (Solution().decrypt([2,4,9,3], -2))
