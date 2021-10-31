package implementation;

import java.util.Arrays;
import java.util.Scanner;

public class 부분합 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        int left = 0;
        int right = 0;
        int result = 100001;
        int sum = 0;
        while(true){
            if(sum>=s){
                sum -= arr[left];
                left += 1;
                result = Math.min(result, right-left+1);
            } else if(right==n){
                break;
            } else {
                sum += arr[right];
                right += 1;
            }
        }
        if(result==100001){
            System.out.println(0);
        }else{
            System.out.println(result);
        }
    }
}
