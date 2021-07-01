package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 아기상어2 {

    static int[] dx = {0,1,1,1,0,-1,-1,-1};
    static int[] dy = {1,1,0,-1,-1,-1,0,1};
    static int n,m;
    static int[][] map;
    static int[][] dist;
    static Queue<Node> q = new LinkedList<>();
    static int result = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        dist = new int[n][m];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                dist[i][j] = Integer.MAX_VALUE;
                if(map[i][j]==1){
                    q.add(new Node(i,j));
                    dist[i][j] = 0;
                }
            }
        }

        while(!q.isEmpty()){
            Node now = q.poll();
            int x = now.x;
            int y = now.y;
            for(int i=0; i<8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<m){
                    if(dist[nx][ny] > dist[x][y]+1){
                        dist[nx][ny] = dist[x][y]+1;
                        q.add(new Node(nx,ny));
                        result = Math.max(result, dist[nx][ny]);
                    }
                }
            }
        }
        System.out.println(result);
    }

    static class Node{
        int x;
        int y;

        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}


