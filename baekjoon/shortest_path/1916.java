package shortest_path;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        int[] distance = new int[n+1];

        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<Node>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            graph.get(v).add(new Node(w,e));
        }

        Arrays.fill(distance, (int)1e9);

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        distance[start] = 0;
        PriorityQueue<Node> q = new PriorityQueue<>();
        q.add(new Node(start, distance[start]));

        while(!q.isEmpty()){
            Node node = q.poll();
            int now = node.index;
            int cost = node.cost;
            if(distance[now] < cost){
                continue;
            }

            for(int i=0; i<graph.get(now).size(); i++){
                int next_cost = distance[now] + graph.get(now).get(i).cost;
                if(next_cost<distance[graph.get(now).get(i).index]){
                    distance[graph.get(now).get(i).index] = next_cost;
                    q.add(new Node(graph.get(now).get(i).index, next_cost));
                }
            }
        }
        System.out.println(distance[end]);
    }
}

class Node implements Comparable<Node>{

    int index;
    int cost;

    public Node(int dest, int cost){
        this.index = dest;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node node){
        return Integer.compare(this.cost, node.cost);
    }
}