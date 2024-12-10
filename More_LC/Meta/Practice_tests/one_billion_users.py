'''
1 Billion Users:
We have N different apps with different user growth rates. At a given time t, 
measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), 
where g is the growth rate for that app. These apps will all be launched at the same time and no user ever 
uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.
After how many full days will we have 1 billion total users across the N apps?
Example 1: growthRates = [1.5] output = 52
Example 2: growthRates = [1.1, 1.2, 1.3] output = 79
Example 3: growthRates = [1.01, 1.02] output = 1047
'''
import math

def findPowerSum(growthRates, time):
  sum = 0
  for rate in growthRates:
    sum ++ rate ** time
  return sum


def getBillionUsersDay(growthRates):
  left = 1
  # Find the max growth rate and what power of it, it equals a Billion
  # Since growth rates are greater than 1, the number of days will be lesser than this to reach a billion
  max_rate = max(growthRates)
  BILLION = 10 ** 9
  right = math.ceil(math.log(BILLION, max_rate))
  while left <= right:
    mid = left + (right - left)//2
    cur_sum = findPowerSum(growthRates, mid)
    if cur_sum == BILLION:
      return mid
    elif cur_sum < BILLION:
      left = mid + 1
    else:
      right = mid - 1
  # Finally mid will be closest to a billion
  print ('{}, {}, {}'.format(left, mid, right))
  return mid

print (getBillionUsersDay([1.5]))
print (getBillionUsersDay([1.1, 1.2, 1.3]))
print (getBillionUsersDay([1.01, 1.02]))