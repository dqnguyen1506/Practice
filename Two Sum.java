import java.util.ArrayList; 
import java.util.Arrays; 
import java.util.List;
import java.util.Map;
import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int[] {i, map.get(complement)};
            }
            map.put(nums[i], i);
        }
        return null;
    }
    public static void main (String[] args){
        int[] nums = new int[]{3,2,4}; 
        Solution sol = new Solution();
        int[] result = sol.twoSum(nums,6);
    }
}