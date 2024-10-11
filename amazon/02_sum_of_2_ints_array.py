'''
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not.
'''

def check_two_sum(arr, t):
    prefix = set()
    # Replace this placeholder return statement with your code
    for i in arr:
      if (t - i) in prefix:
        return True
      else:
        prefix.add(i)
    return False


if __name__ == '__main__':
   arr = [2, 1, 8, 4, 7, 3]
   t = 3
   print(check_two_sum(arr, t))
   arr = [2, 1, 8, 4, 7, 3]
   t = 7
   print(check_two_sum(arr, t))

