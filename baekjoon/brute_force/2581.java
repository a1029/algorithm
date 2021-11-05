package brute_force;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();
        boolean[] arr = new boolean[10001];
        Arrays.fill(arr, true);
        for(int i=2; i<=Math.ceil(Math.sqrt(10001)); i++){
            if (arr[i]){
                int j=2;
                while(i*j<=10000){
                    arr[i*j] = false;
                    j++;
                }
            }
        }

        int result = 0;
        int min = Integer.MAX_VALUE;
        for(int i=m; i<=n; i++){
            if (arr[i] && i>1){
                result += i;
                min = Integer.min(min, i);
            }
        }

        if (result == 0) {
            System.out.println(-1);
        }else{
            System.out.println(result);
            System.out.println(min);
        }
    }
}
