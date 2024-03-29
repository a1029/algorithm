package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n,k;
    static Queue<Node> queue = new LinkedList<>();
    static int[] visit = new int[100001];
    static Stack<Integer> stack = new Stack<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        Arrays.fill(visit, -1);

        bfs();
    }

    public static void bfs(){

        queue.add(new Node(n, 0));
        visit[n] = n;

        while(!queue.isEmpty()){
            Node node = queue.poll();

            if (node.pos==k){
                System.out.println(node.time);
                stack.add(node.pos);
                for(int i=node.pos; i!=n;){
                    stack.add(visit[i]);
                    i = visit[i];
                }
                while(!stack.isEmpty()){
                    System.out.print(stack.pop() + " ");
                }
                break;
            }else{
                int nv1 = node.pos-1;
                int nv2 = node.pos+1;
                int nv3 = node.pos*2;

                if (nv1>=0 && visit[nv1]==-1){
                    visit[nv1] = node.pos;
                    queue.add(new Node(nv1, node.time+1));
                }
                if (nv2 <= 100000 && visit[nv2]==-1){
                    visit[nv2] = node.pos;
                    queue.add(new Node(nv2, node.time+1));
                }
                if (nv3 <= 100000 && visit[nv3]==-1){
                    visit[nv3] = node.pos;
                    queue.add(new Node(nv3, node.time+1));
                }
            }
        }
    }
}