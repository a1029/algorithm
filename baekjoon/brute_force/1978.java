package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double n = Double.parseDouble(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }

        boolean[] x = new boolean[1001];
        for(int i=0; i<1001; i++){
            x[i] = true;
        }
        for(int i=2; i<=Math.ceil(Math.sqrt(1000)); i++){
            if (x[i]){
                int j=2;
                while(i*j<=1000){
                    x[i*j] = false;
                    j++;
                }
            }
        }

        int result=0;
        for (Integer integer : arr) {
                if (x[integer]&&integer>1) {
                    result++;
                }
            }
        System.out.println(result);
    }
}
