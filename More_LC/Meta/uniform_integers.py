'''
A positive integer is considered uniform if all of its digits are equal. For example, 
222 is uniform, while 223 is not.
Given two positive integers 
A and B, determine the number of uniform integers between A and B, inclusive.
'''
def getUniformIntegerCountInInterval(A: int, B: int) -> int:

  cur_len = len(str(A))
  max_len = len(str(B))
  total_result = 0
  result_array = []
  while cur_len <= max_len:
    for cur_dig in range(1,10):
      cur_num = int(str(cur_dig)*cur_len)
      if cur_num < A:
        continue
      elif cur_num > B:
        break
      else:
        total_result += 1
        result_array.append(cur_num)
    cur_len += 1
  print(result_array)
  return total_result

print (getUniformIntegerCountInInterval(75, 375))
print (getUniformIntegerCountInInterval(1,9))
print (getUniformIntegerCountInInterval(999999999999, 999999999999))