'''
LC 735: Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.
Input: asteroids = [5,10,-5] Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
'''
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = stack[-1] + a
                if diff > 0:
                    # If the positive asteroid won, it can no longer 
                    # collide and we end this cycle
                    a = 0
                elif diff < 0:
                    # Since the negative asteroid won, we can pop 
                    # the positive element from the stack
                    stack.pop()
                else:
                    # If both are equal they cancel each other out
                    # In that case we can pop from the stack
                    # and the asteroids can no longer collide
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)
        return stack

collider = Solution().asteroidCollision
print (collider([5,10,-5]))
print (collider([8,-8]))
print (collider([10,2,-5]))
print (collider([-2,-1,1,2]))