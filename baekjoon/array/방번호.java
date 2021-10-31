package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 방번호 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] N = br.readLine().split("");
        int[] count = new int[10];
        Arrays.fill(count, 0);

        for(int i=0; i<N.length; i++){
            int index = Integer.parseInt(N[i]);
            if(index==6 || index==9){
                count[6] += 1;
            } else {
                count[index] += 1;
            }
        }
        int ans1 = Integer.MIN_VALUE;
        int ans2 = Integer.MIN_VALUE;
        for(int i=0; i<10; i++){
            if(i==6){
                ans1 = Math.max(ans1, count[i]);
            } else {
                ans2 = Math.max(ans2, count[i]);
            }
        }
        ans1 = (int)Math.ceil(ans1/(double)2);
        System.out.println(Math.max(ans1, ans2));
    }
}
