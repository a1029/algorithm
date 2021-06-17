package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 최소최대 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int max = -1000001;
        int min = 1000001;
        for(int i=0; i<n; i++){
            int tmp = Integer.parseInt(st.nextToken());
            max = Integer.max(max, tmp);
            min = Integer.min(min, tmp);
        }
        System.out.println(min + " " + max);
    }
}
