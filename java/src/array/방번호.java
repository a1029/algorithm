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

        int answer = 0;
        for(int i=0; i<N.length; i++){
            int index = Integer.parseInt(N[i]);
            count[index] += 1;
        }
        int result = Integer.MIN_VALUE;
        int index = 0;
        for(int i=0; i<10; i++){
            if (result <= count[i]){
                result = count[i];
                index = i;
            }
        }
        if(index==6 || index==9){
            System.out.println((int)Math.ceil(count[index]/(double)2));
        } else {
            System.out.println(count[index]);
        }
    }
}
