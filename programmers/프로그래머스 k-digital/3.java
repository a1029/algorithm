import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.TreeSet;

public class 프로그래머스3 {

    public static int getCount(int n, int start, int[][] graph){

        int count = 1;
        boolean[] visit = new boolean[n+1];
        visit[start] = true;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        while (!q.isEmpty()){
            int now = q.poll();
            for(int next=1; next<n+1; next++){
                if (next!=now && !visit[next]){
                    if(graph[now][next]==1 || graph[next][now]==1){
                        count+=1;
                        q.add(next);
                        visit[next] = true;
                    }
                }
            }
        }
        return count;
    }

    public static int solution(int n, int[][] wires) {

        int answer = (int)1e9;
        TreeSet<Integer> nodes = new TreeSet<>();
        int[][] graph = new int[n+1][n+1];
        for(int[] rows : graph){
            Arrays.fill(rows, 0);
        }

        for(int i=0; i<n-1; i++){
            int from = wires[i][0];
            int to =  wires[i][1];
            graph[from][to] = 1;
            graph[to][from] = 1;
            nodes.add(from);
            nodes.add(to);
        }

        for(int i : nodes){
            for(int j=i+1; j<n+1; j++){
                if (graph[i][j]== 1 || graph[j][i] == 1){
                    graph[i][j] = 0;
                    graph[j][i] = 0;
                    answer = Math.min(answer, Math.abs(getCount(n, i, graph)-getCount(n, j, graph)));
                    graph[i][j] = 1;
                    graph[j][i] = 1;
                }

            }
        }
        return answer;
    }
    public static void main(String[] args) {

        System.out.println(solution(9, new int[][]{{1,3},{2,3},{3,4},{4,5},{4,6},{4,7},{7,8},{7,9}}));
        System.out.println(solution(4, new int[][]{{1,2},{2,3},{3,4}}));
        System.out.println(solution(7, new int[][]{{1,2},{2,7},{3,7},{3,4},{4,5},{6,7}}));
    }
}
