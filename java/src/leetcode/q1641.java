package leetcode;

import java.util.Arrays;

public class q1641 {
    public int countVowelStrings(int n) {

        int a=1, e=1, i=1, o=1, u=1;

        while (--n!=0) {
            o += u;
            i += o;
            e += i;
            a += e;
        }

        return a+e+i+o+u;
    }

    public int countVowelStrings2(int n) {

        int[][] dp = new int[n + 1][6];
        for (int i = 1; i <= n; ++i) {
            for (int k = 1; k <= 5; ++k) {
                dp[i][k] = dp[i][k - 1] + (i > 1 ? dp[i - 1][k] : 1);
            }
        }

        return dp[n][5];
    }

    public int countVowelStrings3(int n) {

        int[] dp = {1,1,1,1,1};

        for (int i=1; i<n; i++) {
            for (int j=1; j<5; j++) {
                dp[j] = dp[j] + dp[j-1];
            }
        }

        return Arrays.stream(dp).sum();
    }


    public static void main(String[] args) {
        q1641 q = new q1641();
    }
}
