'''
LC 1570: DOT Product of 2 Sparse Vectors:
Given two sparse vectors, compute their dot product.
Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse? Use binary search on the list that is not sparse instead of using 2 pointers
'''
class SparseVector:
    def __init__(self, nums: list[int]):
        '''
        # Create a map 
        self.sparse_map = {}
        for id, num in enumerate(nums):
            if num:
                self.sparse_map[id] = num
        '''
        self.sparse_list = []
        for id, num in enumerate(nums):
            if num:
                # self.sparse_map[id] = num
                self.sparse_list.append((id, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # map1, map2 = self.sparse_map, vec.sparse_map
        product = 0
        '''
        if len(map1) > len(map2):
            map1, map2 =  vec.sparse_map, self.sparse_map
        for key, val in map1.items():
            if key in map2:
                product += map1[key] * map2[key]
        '''
        list1, list2 = self.sparse_list, vec.sparse_list
        if len(list1) > len(list2):
            list1, list2 = vec.sparse_list, self.sparse_list
        ptr1 = ptr2 = 0
        while ptr1 < len(list1) and ptr2 < len(list2):
            id1, num1 = list1[ptr1]
            id2, num2 = list2[ptr2]
            if id1 == id2:
                product += list1[ptr1][1] * list2[ptr2][1]
                ptr1 += 1
                ptr2 += 1
            elif id1 < id2:
                ptr1 += 1
            else:
                ptr2 += 1
        return product

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)
print (ans)
v1 = SparseVector([1,0,0,0,0,0,0,0,0,0,2,0,2,3])
v2 = SparseVector([0,0,0,0,0,0,0,0,0,0,3,0,4,0])
ans = v1.dotProduct(v2)
print (ans)

'''
For sparse vectors use 2 pointer approach instead of hash map as it will be more efficient due to collisions
'''