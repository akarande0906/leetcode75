# [1,2,3,4,5,6,7, None, None, 8, 9] 
# Input [1,3,2] => True
# [1,2,3] => True
# [3,1,2] => False
'''
                    6
                4      
            2.           7 
          1.  3            
          [1,3,2,4,7,6,5]          
'''     
def isBST(postOrderArray):
    
    
    def helper(root_id, start_id):
        # Identify left subtree:
        left_root, right_root = -1, -1
        for i in range(root_id -1, start_id - 1, -1):
            if postOrderArray[i] < postOrderArray[root_id]:
                left_root = i
                if left_root != root_id - 1:
                    right_root = root_id - 1
                    break
        if left_root != -1:
            for l in range(0, left_root+1):
                if postOrderArray[l] > postOrderArray[root_id]:
                    return False 
            helper(left_root, 0)
        if right_root != -1:
            helper(right_root, left_root + 1)
        return True
                               
        
    root_id = len(postOrderArray) - 1
    return helper(root_id)
        
        

