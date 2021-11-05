package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n,k;
    static int time = Integer.MAX_VALUE;
    static Queue<Node> queue = new LinkedList<>();
    static HashMap<Integer, Integer> map = new HashMap<>();
    static boolean[] visit = new boolean[100001];
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        if (n>k){
            System.out.println(n-k);
            System.out.println(1);
        } else {
            bfs();
            System.out.println(time);
            System.out.println(map.get(time));
        }
    }

    public static void bfs(){

        queue.add(new Node(n,0));

        while(!queue.isEmpty()){
            Node node = queue.poll();
            visit[node.pos] = true;
            if (node.pos==k){
                map.put(node.time, map.getOrDefault(time, 0)+1);
                time = Math.min(time, node.time);
            }else{
                int nv1 = node.pos-1;
                int nv2 = node.pos+1;
                int nv3 = node.pos*2;

                if (nv1>=0 && !visit[nv1]){
                    queue.add(new Node(nv1, node.time+1));
                }
                if (nv2 <= 100000 && !visit[nv2]){
                    queue.add(new Node(nv2, node.time+1));
                }
                if (nv3 <= 100000 && !visit[nv3]){
                    queue.add(new Node(nv3, node.time+1));
                }
            }
        }
    }
}

class Node{

    int pos;
    int time;

    public Node(int pos, int time){
        this.pos = pos;
        this.time = time;
    }
}
