'''
Given an array of distinct positive integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
'''

def combinationSum(coins, target):
   res = []
   cur_arr = []

   def backtrack(coins, target, cur_ptr):
      if target  == 0: # Terminating condition
         res.append(cur_arr.copy()) # Create a copy. Dont directly dump the array : or list(cur_arr)
         return
      for i in range(cur_ptr, len(coins)):
         if coins[i] > target:
            continue
         cur_arr.append(coins[i])
         backtrack(coins, target - coins[i], i)
         cur_arr.pop() # backtrack


   backtrack(coins, target, 0)
   return res

coins = [2, 3, 6, 7]
target = 7
print(combinationSum(coins, target))
      
coins = [2, 3, 5]
target = 8
print(combinationSum(coins, target))

coins = [5, 10, 15]
target = 20
print(combinationSum(coins, target))
