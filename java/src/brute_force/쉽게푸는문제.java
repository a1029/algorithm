package brute_force;

import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 쉽게푸는문제 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        ArrayList<Integer> arr = new ArrayList<>();
        int i=1;
        while (arr.size()<1001){
            int count = i;
            while (count>0){
                arr.add(i);
                count-=1;
            }
            i+=1;
        }

        int result = 0;
        for(int j=a; j<=b; j++){
            result += arr.get(j-1);
        }
        System.out.println(result);
    }
}
