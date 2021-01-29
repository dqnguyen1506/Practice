import java.util.Arrays;
import java.util.List;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] arr = new char[s.length()];
        for (int i = 0; i < s.length(); i++){
            arr[i] = Arrays.asList(arr).contains(s.charAt(i)) ? continue : s.charAt(i);
        }
        return 0;
    }
    public static void main(String[] args){
        Solution sol = new Solution();
        sol.lengthOfLongestSubstring("abc");
    }
}