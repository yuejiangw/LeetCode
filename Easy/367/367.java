class Solution {
    public boolean isPerfectSquare(int num) {
        int i = 0;
        int j = num;
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if ((long) mid * mid == num) {
                return true;
            } else if ((long) mid * mid < num) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }
        return false;
    }
}