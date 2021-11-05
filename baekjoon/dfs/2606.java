package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 바이러스 {

    static int n,k;
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static int result = 0;
    static boolean[] visit;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        for(int i=0; i<n+1; i++){
            arr.add(new ArrayList<>());
        }
        for(int i=0; i<k; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
            arr.get(b).add(a);
        }

        visit = new boolean[n+1];
        dfs(1);
        System.out.println(result-1);
    }

    public static void dfs(int now){
        visit[now] = true;
        result += 1;
        for(int next : arr.get(now)){
            if(!visit[next]){
                dfs(next);
            }
        }
    }
}
