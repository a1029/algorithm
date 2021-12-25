package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static char[][] map;
    static boolean[][] visit;
    static int n,m;
    static int a=0,b=0;
    static int count = 0;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new char[m][n];
        visit = new boolean[m][n];

        for(boolean[] v : visit){
            Arrays.fill(v, false);
        }

        for(int i=0; i<m; i++){
            String line = br.readLine();
            for(int j=0; j<n; j++){
                map[i][j] = line.charAt(j);;
            }
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if (!visit[i][j]){
                    count = 0;
                    int result = dfs(i,j,map[i][j]);
                    if (map[i][j]=='W'){
                        a += result*result;
                    }else{
                        b += result*result;
                    }
                }
            }
        }
        System.out.println(a + " " + b);
    }

    public static int dfs(int x, int y, char prev){

        if (x<0 || x>=m || y<0 || y>=n || visit[x][y] || prev!=map[x][y]){
            return 0;
        }
        count += 1;
        visit[x][y] = true;
        dfs(x,y+1, prev);
        dfs(x,y-1, prev);
        dfs(x+1,y, prev);
        dfs(x-1,y, prev);

        return count;
    }
}
