'''
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. 
'''
def find_missing(nums):
  
    n = len(nums) + 1
    exp_total = n * (n+1) // 2
    total = 0
    for i in nums:
      total += i
    return exp_total - total

if __name__ == '__main__':
    arr = [3,7,1,2,8,4,5]
    print(find_missing(arr))
    arr = [1,3,5,7,9,2,4,6]
    print(find_missing(arr))
