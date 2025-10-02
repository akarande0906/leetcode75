def coinChangeWays(coins, amount):
  dp = [0] * (amount+1)
  dp[0] = 1
   
  
  for i in range(1, amount+1): 
    for coin in coins:
      if i - coin < 0:
        continue
      dp[i] += dp[i-coin]

  return dp[amount]

def coinChangeWaysMemo(coins, amount):
  memo = {0: 1}
  def coinChangeHelper(change):
    answer = 0
    if change in memo:
      return memo[change]
    if change == 0:
      answer = 1 
    else:
      for coin in coins:
        if change - coin < 0:
          continue
        answer += coinChangeHelper(change - coin) 
    memo[change] = answer
    return answer
  return coinChangeHelper(amount)


print(coinChangeWays([1,2,5],5))
print(coinChangeWays([1,4,5],5))
print(coinChangeWays([1,2,5],150))
print(coinChangeWays([1,4,5,8],87))

print(coinChangeWaysMemo([1,2,5],5))
print(coinChangeWaysMemo([1,4,5],5))
print(coinChangeWaysMemo([1,2,5],150))
print(coinChangeWays([1,4,5,8],87))
