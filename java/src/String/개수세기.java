package String;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 개수세기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.parseInt(br.readLine());
        int result = 0;
        while(st.hasMoreTokens()){
            int t = Integer.parseInt(st.nextToken());
            if (v==t){
                result += 1;
            }
        }
        System.out.println(result);
    }
}
