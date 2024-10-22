def coinChange(coins, amount):
  dp = [0] * (amount+1)
  dp[0] = 1
   
  for coin in coins:
    for i in range(coin, amount+1): 
      dp[i] += dp[i-coin]

  return dp[amount]


print(coinChange([1,2,5],5))
