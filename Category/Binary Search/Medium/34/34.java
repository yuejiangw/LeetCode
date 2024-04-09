class Solution {
    private int findLeft(int[] nums, int target) {
        int i = 0;
        int j = nums.length;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (nums[mid] >= target) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        return nums[i] == target ? i : -1;
    }

    private int findRight(int[] nums, int target) {
        int i = 0;
        int j = nums.length;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (nums[mid] <= target) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        int res = i - 1;
        return nums[res] == target ? res : -1;
    }

    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0 || target < nums[0] || target > nums[nums.length - 1]) {
            return new int[] {-1, -1};
        }
        int[] res = new int[2];
        res[0] = findLeft(nums, target);
        res[1] = findRight(nums, target);
        return res;
    } 
}