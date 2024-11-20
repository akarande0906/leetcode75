'''
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
'''
def icecreamParlor(m, arr):
    # Write your code here
    ic_cost_map = {}
    for index in range(len(arr)):
        if m - arr[index] in ic_cost_map:
            return [ic_cost_map[m - arr[index]] + 1, index + 1]
        else:
            ic_cost_map[arr[index]] = index
    return []

print (icecreamParlor(6, [1,3,4,5,6]))
            