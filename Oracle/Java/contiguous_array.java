package Oracle.Java;

// Leet Code 525: Contiguous Array

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> count_map = new HashMap<Integer, Integer>();
        count_map.put(0, -1); // Base condition
        int cur_count = 0;
        int max_length = 0;
        for (int i = 0; i < nums.length; i++) {
            cur_count = (nums[i] == 1) ? cur_count+1 : cur_count-1;
            if (count_map.containsKey(cur_count)) {
                int window = i - count_map.get(cur_count);
                if (window > max_length) {
                    max_length = window;
                }
            } else {
                count_map.put(cur_count, i);
            }
        }
        return (max_length);

        
    }

    public static void main(String args[]) {
        Solution sol = new Solution();
        int[] arr = {0,1};
        System.out.println(sol.findMaxLength(arr));
        int[] arr2 = {0,1,1,1,1,1,0,0,0};
        System.out.println(sol.findMaxLength(arr2));

    }
}


