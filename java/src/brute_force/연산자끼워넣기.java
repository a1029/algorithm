package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 연산자끼워넣기 {

    public static int max = Integer.MIN_VALUE;
    public static int min = Integer.MAX_VALUE;
    public static int add = 0;
    public static int sub = 0;
    public static int mul = 0;
    public static int div = 0;
    public static int[] arr;
    public static int n;
    public static StringTokenizer st;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        add = Integer.parseInt(st.nextToken());
        sub = Integer.parseInt(st.nextToken());
        mul = Integer.parseInt(st.nextToken());
        div = Integer.parseInt(st.nextToken());

        dfs(arr[0],1);
        System.out.println(max);
        System.out.println(min);
    }

    public static void dfs(int prev, int index){
        if(index==n){
            max = Integer.max(max,prev);
            min = Integer.min(min,prev);
            return;
        }

        if(add>0){
            add-=1;
            dfs(prev+arr[index], index+1);
            add+=1;
        }
        if(sub>0){
            sub-=1;
            dfs(prev-arr[index],index+1);
            sub+=1;
        }
        if(mul>0){
            mul-=1;
            dfs(prev*arr[index],index+1);
            mul+=1;
        }
        if(div>0){
            div-=1;
            dfs(prev/arr[index], index+1);
            div+=1;
        }
    }
}
