package leetcode;

import java.util.Arrays;

public class q31 {
    public void nextPermutation(int[] nums) {

        int idx = nums.length - 2;
        while (idx >= 0 && nums[idx] >= nums[idx+1]) {
            idx -= 1;
        }

        if (idx == -1) {
            Arrays.sort(nums);
        } else {
            for (int i = nums.length - 1; i > idx; i--) {
                if (nums[i] > nums[idx]) {
                    int tmp = nums[i];
                    nums[i] = nums[idx];
                    nums[idx] = tmp;
                    Arrays.sort(nums, idx + 1, nums.length);
                    return;
                }
            }
        }
    }

    public static void main(String[] args) {
        q31 q = new q31();

        int[] nums = new int[]{5,1,1};
        q.nextPermutation(nums);
        System.out.println(Arrays.toString(nums));
    }
}
