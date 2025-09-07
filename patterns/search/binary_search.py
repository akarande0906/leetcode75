def binary_search(arr, low, high, key):
   if low <= high:
      mid = (high+low)//2
      if arr[mid] == key:
         return mid
      elif arr[mid] > key:
         return binary_search(arr, low, mid - 1, key)
      else:
         return binary_search(arr, low + 1, high, key)
   else:
      return -1 

if __name__ == '__main__':
   arr = [ 2, 3, 4, 10, 40 ]
   x = 10
 
   # Function call
   result = binary_search(arr, 0, len(arr)-1, x)
 
   if result != -1:
       print("Element is present at index", str(result))
   else:
       print("Element is not present in array")
