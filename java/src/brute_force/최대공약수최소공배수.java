package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 최대공약수최소공배수 {

    public static void main(String[] args) throws IOException {

        int a=0,b=0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        int min=0,max=0;
        int i=1;
        for(;i<=a&&i<=b;){
            if (a % i == 0 && b % i == 0) {
                min=i;
            }
            i++;
        }
        max = a*b/min;
        System.out.println(min);
        System.out.println(max);
    }
}
