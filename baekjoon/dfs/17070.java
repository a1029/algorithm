package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 파이프옮기기1 {

    public static int result = 0;
    public static int n = 0;
    public static int[][] map;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        for(int i=0; i<n; i++){
            String[] tmp = br.readLine().split(" ");
            for(int j=0; j<n; j++){
                map[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        dfs(0,1,0);
        System.out.println(result);
    }

    public static void dfs(int x, int y, int shape){
        if (x==n-1 && y==n-1){
            result += 1;
            return;
        }
        if (shape==0 || shape==2){
            if (y+1<n && map[x][y+1]==0){
                dfs(x,y+1,0);
            }
        }
        if (shape==1 || shape==2){
            if (x+1<n && map[x+1][y]==0){
                dfs(x+1,y,1);
            }
        }
        if (shape==0 || shape==1 || shape==2){
            if (x+1<n && y+1<n && map[x+1][y]==0 && map[x][y+1]==0 && map[x+1][y+1]==0){
                dfs(x+1,y+1,2);
            }
        }
    }
}
