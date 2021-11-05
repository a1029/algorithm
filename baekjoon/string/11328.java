package string;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());
        while(tc-->0){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String[] a = st.nextToken().split("");
            String[] b = st.nextToken().split("");
            int[] count = new int[26];
            Arrays.fill(count, 0);
            for(String s : a){
                count[s.charAt(0)-'a'] += 1;
            }
            for(String s : b){
                count[s.charAt(0)-'a'] -= 1;
            }

            boolean flag = false;
            for(int c : count){
                if(c!=0){
                    System.out.println("Impossible");
                    flag = true;
                    break;
                }
            }
            if(!flag){
                System.out.println("Possible");
            }
        }
    }
}
