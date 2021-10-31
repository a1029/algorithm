package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 방배정 {

    public static void main(String[] args) throws IOException {

        int answer = 0;
        int[][] arr = new int[2][6];
        for(int[] row : arr){
            Arrays.fill(row, 0);
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        for(int i=N; i>0; i--){
            st = new StringTokenizer(br.readLine());
            int S = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());

            if(arr[S][Y-1]==K){
                arr[S][Y-1] = 1;
                answer += 1;
            } else if(arr[S][Y-1]==0){
                arr[S][Y-1] += 1;
                answer += 1;
            } else {
                arr[S][Y-1] += 1;
            }
        }
        System.out.println(answer);
    }
}
