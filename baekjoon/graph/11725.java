import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i=1; i<=n; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<n-1; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        int[] parent = new int[n+1];
        Boolean[] visit = new Boolean[n+1];
        Arrays.fill(parent, -1);
        Arrays.fill(visit, false);
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        visit[1] = true;
        while(!queue.isEmpty()){
            int now = queue.poll();
            for(int child : graph[now]){
                if(!visit[child]){
                    parent[child] = now;
                    queue.add(child);
                    visit[child] = true;
                }
            }
        }

        for(int i=2; i<=n; i++){
            System.out.println(parent[i]);
        }
    }
}
