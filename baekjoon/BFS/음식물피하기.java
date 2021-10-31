package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 음식물피하기 {

    static int n,m,k;
    static int[][] map;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean[][] visit;
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        visit = new boolean[n][m];

        for(int i=0; i<k; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            map[a-1][b-1] = 1;
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if (!visit[i][j] && map[i][j]==1){
                    bfs(new Point(i,j));
                }
            }
        }
        System.out.println(result);
    }

    public static void bfs(Point node){

        int count = 1;
        Queue<Point> q = new LinkedList<>();
        q.add(node);
        visit[node.x][node.y] = true;
        while(!q.isEmpty()){
            Point now = q.poll();
            int x = now.x;
            int y = now.y;
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0<=nx && nx < n && 0<=ny && ny < m && !visit[nx][ny] && map[nx][ny]==1){
                    visit[nx][ny] = true;
                    count += 1;
                    q.add(new Point(nx,ny));
                }
            }
        }
        result = Math.max(result, count);
    }
}

class Point{

    public int x;
    public int y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}
