import jdk.incubator.jpackage.internal.Arguments;

import java.math.*;
class Solution {
    public int reverse (int x){
        String converted = String.valueOf(Math.abs(x));
        //System.out.println(converted);
        String rev = "";
        for (int i = converted.length() - 1; i >= 0; i--){
            //System.out.println(converted.charAt(i));
            rev += converted.charAt(i);
        }
        try{
            return (x < 0) ? Integer.parseInt(rev) * -1 : Integer.parseInt(rev);
        }
        catch(NumberFormatException e){
            return 0;
        } 
    }
    public static void main (String[] args){
        Solution sol = new Solution();
        System.out.println(sol.reverse(153423649));
    }
}