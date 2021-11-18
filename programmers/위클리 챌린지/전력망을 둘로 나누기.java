import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    
    public static int count = 0;
    public static boolean[] visit;
    
    public int solution(int n, int[][] wires) {
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        visit = new boolean[n+1];

        int answer = Integer.MAX_VALUE;

        for(int i=0; i<n+1; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<wires.length; i++){
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
        }

        for(int i=0; i<wires.length; i++){
            graph[wires[i][0]].remove(Integer.valueOf(wires[i][1]));
            graph[wires[i][1]].remove(Integer.valueOf(wires[i][0]));
            count = 1;
            Arrays.fill(visit, false);
            int count1 = dfs(graph, wires[i][0], visit);
            count = 1;
            Arrays.fill(visit, false);
            int count2 = dfs(graph, wires[i][1], visit);
            System.out.println(count1 + " " + count2 + " " + i);
            answer = Math.min(Math.abs(count1-count2), answer);
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
        };
        return answer;
    }
    
    public static int dfs(ArrayList<Integer>[] graph, int root, boolean[] visit){

        visit[root] = true;
        for(int next : graph[root]){
            if(!visit[next]) {
                visit[next] = true;
                count += 1;
                dfs(graph, next, visit);
            }
        }
        return count;
    }
}
