class Solution {
    public int mySqrt(int x) {
        int i = 0;
        // j = x 而不是 x + 1因为容易有越界问题，当x = 2^31 -1时j = x + 1会变成0
        int j = x;
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if ((long) mid * mid == x) {
                return mid;
            } else if ((long) mid * mid < x) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        return i - 1; 
    }
}