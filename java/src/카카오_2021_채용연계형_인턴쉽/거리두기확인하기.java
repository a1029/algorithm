package 카카오_2021_채용연계형_인턴쉽;

import java.util.*;
import java.util.stream.IntStream;

public class 거리두기확인하기 {

    public static void main(String[] args) {
        String[][] input = {
                {"OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"},
                {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}};
        System.out.println(Arrays.toString(solution(input)));
    }

    public static int[] solution(String[][] places) {

        int[] answer = new int[places.length];
        IntStream.range(0,places.length).forEach(i -> {
            answer[i] = bfs(places[i]) ? 1 : 0;
        });
        return answer;
    }


    public static boolean bfs(String[] p){
        String[][] graph = new String[5][5];
        for(int i=0; i<5; i++){
            graph[i] = p[i].split("");
        }

        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};

        ArrayList<int[]> poses = new ArrayList<>();
        for(int i=0; i<5; i++){
            for(int j=0; j<5; j++){
                if(graph[i][j].equals("P")){
                    poses.add(new int[]{i,j,0});
                }
            }
        }

        for(int[] start : poses){
            boolean[][] visited = new boolean[5][5];
            for(boolean[] row : visited){
                Arrays.fill(row, false);
            }
            visited[start[0]][start[1]] = true;
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{start[0],start[1],start[2]});
            boolean flag = true;
            while(!q.isEmpty()){
                int[] pos = q.poll();
                int x = pos[0], y = pos[1], d = pos[2];
                for(int i=0; i<4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx<0 || nx>=5 || ny<0 || ny>=5){
                        continue;
                    }
                    if(d+1>2 || graph[nx][ny].equals("X") || visited[nx][ny]){
                        continue;
                    }
                    if(graph[nx][ny].equals("P")){
                        flag = false;
                    } else if(graph[nx][ny].equals("O")){
                        visited[nx][ny] = true;
                        q.add(new int[]{nx,ny,d+1});
                    }
                }
            }
            if(!flag) {
                return false;
            }
        }
        return true;
    }
}
