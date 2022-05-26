package leetcode;

public class q45 {

    public int jump(int[] nums) {

        int count = 0;
        int pos = 0;

        while (pos < nums.length - 1) {
            int maxValue = -1;
            int maxIndex = -1;
            for (int i=pos+1; i<=pos+nums[pos] && i<nums.length; i++) {
                if (i == nums.length-1) {
                    return count + 1;
                }

                if (i + nums[i] >= maxValue) {
                    maxValue = i + nums[i];
                    maxIndex = i;
                }
            }
            pos = maxIndex;
            count += 1;
        }
        return count;
    }

    public int jump2(int[] nums) {
        int count = 0;
        int now = 0;
        int max = 0;
        for (int i=0; i<nums.length-1; i++) {
            max = Integer.max(max, i + nums[i]);
            if (i == now) {
                count += 1;
                now = max;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        q45 q = new q45();
        //System.out.println(q.jump(new int[]{2,3,1,1,4}));
        System.out.println(q.jump(new int[]{3,2,1}));

        System.out.println(q.jump2(new int[]{10,9,8,7,6,5,4,3,2,1,1,0}));
    }
}
