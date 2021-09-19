package 카카오_2021_채용연계형_인턴쉽;

import java.util.HashMap;
import java.util.PriorityQueue;

public class 미로탈출 {

    static int[][] graph = new int[1001][1001];
    static boolean[][] visit = new boolean[1001][1<<10];
    static final int INF = Integer.MAX_VALUE;
    static PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->a[0]-b[0]);

    public static void main(String[] args){
        System.out.println(solution(3,1,3,new int[][]{{1, 2, 2}, {3, 2, 3}}, new int[]{2}));
        System.out.println(solution(4,1,4,new int[][]{{1, 2, 1}, {3, 2, 1}, {2, 4, 1}}, new int[]{2, 3}));
    }

    public static int dijkstra(int n, int src, int dst, int[] traps){

        q.add(new int[]{0, src, 0});
        while(!q.isEmpty()){
            int[] curr = q.poll();
            int w = curr[0];
            int u = curr[1];
            int state = curr[2];

            if(u==dst){
                return w;
            }
            if(visit[u][state]){
                continue;
            }
            visit[u][state] = true;

            boolean currTrapped = false;
            HashMap<Integer, Boolean> trapped = new HashMap<>();
            for(int i=0; i<traps.length; i++){
                int bit = 1 << i;
                if((state & bit) != 0){
                    if(traps[i]==u){
                        state &= ~bit;
                    } else {
                        trapped.put(traps[i], true);
                    }
                } else {
                    if(traps[i]==u){
                        state |= bit;
                        trapped.put(traps[i], true);
                        currTrapped = true;
                    }
                }
            }

            for(int v=1; v<=n; v++){
                if(v==u){
                    continue;
                }
                boolean nextTrapped = trapped.containsKey(v);
                if(currTrapped == nextTrapped) {
                    if(graph[u][v] != INF){
                        q.add(new int[]{w + graph[u][v], v, state});
                    }
                } else {
                    if(graph[v][u] != INF){
                        q.add(new int[]{w + graph[v][u], v, state});
                    }
                }
            }
        }
        return INF;
    }

    public static int solution(int n, int start, int end, int[][] roads, int[] traps) {

        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(i==j){
                    graph[i][j] =0;
                } else {
                    graph[i][j] = INF;
                }
            }
        }
        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int w = road[2];
            if(w < graph[u][v]){
                graph[u][v] = w;
            }
        }

        int answer = dijkstra(n, start, end, traps);
        return answer;
    }
}
