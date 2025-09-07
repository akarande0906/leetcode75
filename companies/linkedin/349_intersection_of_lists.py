class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # First store elements of nums1 in a set
        unique_elems = set(nums1)
        intersect_list = []
        for number in nums2:
            if number in unique_elems:
                intersect_list.append(number)
                unique_elems.remove(number)
        return intersect_list

    print(Solution().intersection([1,2,2,1],[2,2]))
    print(Solution().intersection([4,9,5],[9,4,9,8,4]))


    ''' Alternative solution

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # First store elements of nums1 in a set
        unique_elems1 = set(nums1)
        unique_elems2 = set(nums2)
        intersect_list = []
        for number in unique_elems2:
            if number in unique_elems1:
                intersect_list.append(number)
        return intersect_list

    '''
