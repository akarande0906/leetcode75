'''
Hacker Rank: Equal Stacks
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until 
they are all the same height, then return the height.
Example: h1 = [3,2,1,1,1] h2 = [4,3,2], h3=[1,1,4,1]
Removing from the left: [2,1,1,1], [3,2], [4,1] => h = 5 
'''
def equalStacks(h1, h2, h3):
    ht1 = sum(h1)
    ht2 = sum(h2)
    ht3 = sum(h3)
    
    while True:
        if not ht1 or not ht2 or not ht3: 
            return 0
        if ht1 == ht2 and ht2 == ht3:
            return ht1
        max_ht = max(ht1, ht2, ht3)
        if ht1 == max_ht:
            ht1 = ht1 - h1.pop(0)
        elif ht2 == max_ht:
            ht2 = ht2 - h2.pop(0)
        else:
            ht3 = ht3 - h3.pop(0)
    
print (equalStacks([3,2,1,1,1], [4,3,2], [1,1,4,1]))
print (equalStacks([1,2,3], [3,2,1], [1,1,1]))
print (equalStacks([1,1,1], [3,2,1], [1,2,3]))