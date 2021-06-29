package dfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class DFS와BFS {

    static int n,m,v;
    static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
    static boolean[] visited;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        for(int i=0; i<n+1; i++){
            arr.add(new ArrayList<>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
            arr.get(b).add(a);
        }

        for(int i=1; i<n+1; i++){
            Collections.sort(arr.get(i));
        }

        visited = new boolean[n+1];

        Arrays.fill(visited, false);
        dfs(v);
        System.out.println("");
        Arrays.fill(visited, false);
        bfs(v);
    }

    public static void dfs(int v){
        visited[v] = true;
        System.out.print(v + " ");
        for(int next : arr.get(v)){
            if (!visited[next]){
                dfs(next);
            }
        }
    }

    public static void bfs(int v){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visited[v] = true;
        while(!queue.isEmpty()){
            int now = queue.poll();
            System.out.print(now + " ");
            for(int next : arr.get(now)){
                if (!visited[next]){
                    visited[next] = true;
                    queue.add(next);
                }
            }
        }
    }
}
