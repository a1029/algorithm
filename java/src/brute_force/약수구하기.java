package brute_force;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class 약수구하기 {

    public static void main(String[] args) throws Exception {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayList<Integer> result = new ArrayList<>();
        for(int i=1; i<=n; i++){
            if (n%i==0){
                result.add(i);
            }
        }

        if (result.size()<k){
            System.out.println(0);
        }else{
            System.out.println(result.get(k-1));
        }

    }
}
