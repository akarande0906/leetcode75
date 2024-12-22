'''
LC 134: Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once 
in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
Example 1: Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2] Output: 3  
Example 2: Input: gas = [2,3,4], cost = [3,4,3] Output: -1 : No option to start any station
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

whichPath = Solution().canCompleteCircuit
print (whichPath([1,2,3,4,5], [3,4,5,1,2]))
print (whichPath([2,3,4], [3,4,3]))
print (whichPath([1,2,3,4,5], [5,4,2,1,3]))
print (whichPath([40,40,40,40,40], [20,100,10,40,30]))
    
