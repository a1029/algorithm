package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PuyoPuyo {

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static char[][] map = new char[12][6];
    static boolean[][] visit = new boolean[12][6];
    static int result = 0;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i=0; i<12; i++){
            map[i] = br.readLine().toCharArray();
        }

        while(true){
            boolean continueFlag = false;
            for(boolean[] v : visit){
                Arrays.fill(v, false);
            }
            for(int i=0; i<12; i++){
                for(int j=0; j<12; j++){
                    if(map[i][j]!='.' && !visit[i][j]){
                        HashSet<Node> set = bfs(new Node(i,j));
                        if (set!=null){
                            for (Node node : set) {
                                map[node.x][node.y] = '.';
                            }
                            continueFlag = true;
                            result = Math.max(result, set.size());
                        }
                    }
                }
            }
            if(!continueFlag){
                System.out.println(result);
                break;
            }
        }
    }

    public static HashSet<Node> bfs(Node node){

        int length = 1;
        Queue<Node> q = new LinkedList<>();
        HashSet<Node> posList = new HashSet<>();
        q.add(node);
        posList.add(node);
        visit[node.x][node.y] = true;
        while(!q.isEmpty()){
            Node now = q.poll();
            int x = now.x;
            int y = now.y;
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0<=nx && nx<12 && 0<=ny && ny<6){
                    if(!visit[nx][ny] && map[x][y]==map[nx][ny]){
                        visit[nx][ny] = true;
                        length += 1;
                        q.add(new Node(nx,ny));
                        posList.add(new Node(nx,ny));
                    }
                }
            }
        }

        if (length>=4){
            return posList;
        } else {
            return null;
        }
    }

    public static class Node{
        int x;
        int y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}
