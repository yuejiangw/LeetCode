// class Solution {
//     public boolean containsDuplicate(int[] nums) {
//         return Arrays.stream(nums).distinct().count() < nums.length;
//     }
// }

// java Set自带去重，如果去重后的长度小于原长度，则返回true
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> result = new HashSet<>();
        for (int i : nums) {
            result.add(i);
        } 
        return result.size() < nums.length ? true : false;
    }
}