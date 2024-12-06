def binary_search( nums: list[int], k: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
        
    while left < right:
        mid = right - (right - left) // 2
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1,2,3,4,5]
print (binary_search(arr, 3))
print (binary_search(arr, 2))
print (binary_search(arr, 6))
                
