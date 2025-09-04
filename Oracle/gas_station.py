'''
LC 134: Gas Station
'''
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Can use greedy approach here
        # Check diff at each step to see if enough gas is there to get to the next step
        # if we end up with -ive gas it means we have to consider a different station
        start = 0
        total = 0
        if sum(gas) < sum(cost):
            # If we have a total gas lesser than the cost this will fail
            return -1
        for stn in range(len(gas)):
            total += gas[stn] - cost[stn]
            if total < 0:
                total = 0
                start = stn + 1
        return start
    
# Time Complexity: O(n)
# Space Complexity: O(1) # We are not allotting any extra space. 

sol = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5], [2,3,4,5,1])) # 4
print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(sol.canCompleteCircuit([2,3,4], [3,4,3])) # -1
print(sol.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])) # 4