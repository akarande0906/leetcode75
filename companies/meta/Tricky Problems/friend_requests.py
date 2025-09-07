'''
LC 825: Friends of appropriate ages
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.
Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
Return the total number of friend requests made.
'''
from collections import defaultdict
class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        age_map = defaultdict(int)
        # Create an age map based on age
        for age in ages:
            age_map[age] += 1
        count = 0
        for ageA in age_map:
            for ageB in age_map:
                # Compare ageA with ageB based on the criteria
                # Add the total number of friend reqs
                if (0.5 * ageA + 7) < ageB and ageB <= ageA and (ageB <= 100 or ageA >= 100):
                    count += age_map[ageA] * age_map[ageB]
                    # If the two ages match it means they are the same 
                    # element we are comparing, so subtract that amount
                    if ageA == ageB:
                        count -= age_map[ageA]
        return count

numFriends = Solution().numFriendRequests
print (numFriends([16,16]))
print (numFriends([16,17,18]))
print (numFriends([20,30,100,110,120]))

        