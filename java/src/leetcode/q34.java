package leetcode;

import java.util.Arrays;

public class q34 {

    public int[] searchRange(int[] nums, int target) {

        int tmp = -1;
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                tmp = mid;
                break;
            }
        }

        if (tmp == -1) {
            return new int[]{-1,-1};
        } else {
            left = tmp;
            right = tmp;
            while (left >= 0 && nums[left] == target) {
                left -= 1;
            }
            while (right <= nums.length-1 && nums[right] == target) {
                right += 1;
            }
            return new int[]{left+1, right-1};
        }
    }

    public static void main(String[] args) {

        q34 q = new q34();
        //System.out.println(Arrays.toString(q.searchRange(new int[]{5,7,7,8,8,10}, 8)));
        //System.out.println(Arrays.toString(q.searchRange(new int[]{5,7,7,8,8,10}, 6)));
        //System.out.println(Arrays.toString(q.searchRange(new int[]{}, 0)));
        System.out.println(Arrays.toString(q.searchRange(new int[]{1}, 1)));
    }
}
