import java.lang.Math; 
class Solution {
    public int reverse(int x) {
        int num = x, result = 0;
        int length = String.valueOf((int)Math.abs(x)).length();
        int scale = (int) Math.pow(10, length - 1);
        while (num != 0){
            num = x % 10;
            x /= 10;
            //System.out.println(num);
            if ( result > Integer.MAX_VALUE || length >= 9 && num > 8){
                return 0;
            }
            if (result < Integer.MIN_VALUE || length >= 9 && num < -8){
                return 0;
            }
            result = result + num * scale;
            scale /= 10;
            //System.out.println(result);
            num = x;
            //System.out.println(num);
        }

        return result;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int num = sol.reverse(2147483647); //1534236469 2147483412
        System.out.println(num);
    }
}