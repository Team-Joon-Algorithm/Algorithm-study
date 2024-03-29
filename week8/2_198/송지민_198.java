public class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int robbedPrevious = 0;
        int didNotRobPrevious = 0;

        for (int i = 0; i < nums.length; i++) {
            int currentNotRobbed = Math.max(robbedPrevious, didNotRobPrevious);

            int currentIsRobbed = didNotRobPrevious + nums[i];

            didNotRobPrevious = currentNotRobbed;
            robbedPrevious = currentIsRobbed;
        }

        return Math.max(robbedPrevious, didNotRobPrevious);
    }
}