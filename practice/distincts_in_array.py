class Solution:
    def distincts_in_array(self, array):
        # First sort the array
        if not array:
            return None
        array.sort()
        ret_array = [array[0]]
        for i in range(1, len(array)):
            if array[i] > array[i-1]:
                ret_array.append(array[i])
        return ret_array

    def distincts_in_array_shortcut(self,array):
        if not array:
            return None
        aset = set(array)
        return list(aset)

print (Solution().distincts_in_array([12, 10, 9, 45, 2, 10, 10, 45]))
print (Solution().distincts_in_array([1, 2, 3, 4, 5]))
print (Solution().distincts_in_array([1, 1, 1, 1, 1]))
print (Solution().distincts_in_array_shortcut([12, 10, 9, 45, 2, 10, 10, 45]))
print (Solution().distincts_in_array_shortcut([1, 2, 3, 4, 5]))
print (Solution().distincts_in_array_shortcut([1, 1, 1, 1, 1]))
