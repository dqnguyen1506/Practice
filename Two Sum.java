'''
Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
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
            if(map.containsKey(complement) && nums[map.get(complement)] != nums[i]){
                return new int[] {i, map.get(complement)};
            }
            map.put(nums[i], i);
        }
        return null;
    }
    public static void main (String[] args){
        int[] nums = new int[]{3,2,4}; 
        Solution sol = new Solution();
        for (int i : result){
            System.out.println(i);
        }
        int[] result = sol.twoSum(nums,6);
    }
}