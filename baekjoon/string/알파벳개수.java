package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 알파벳개수 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] result = new int[26];
        Arrays.fill(result, 0);
        String[] str = br.readLine().split("");
        for(String c : str){
            result[c.charAt(0)-97] += 1;
        }
        for(int count: result){
            System.out.print(count + " ");
        }
    }
}
