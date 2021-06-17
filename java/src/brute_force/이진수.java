package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 이진수 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i=0; i<t; i++){
            int n = Integer.parseInt(br.readLine());
            String b = Integer.toBinaryString(n);
            for(int j=b.length()-1; j>-1; j--){
                if (b.charAt(j)=='1'){
                    System.out.print(b.length()-1-j + " ");
                }
            }
            System.out.println("");
        }
    }
}
