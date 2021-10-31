package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class AB {

    static long a,b;
    static Queue<Pair> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        queue.add(new Pair(a,0));
        while(!queue.isEmpty()){
            Pair node = queue.poll();
            if (node.value==b){
                System.out.println(node.count+1);
                return;
            }
            long nv1 = node.value*2;
            long nv2 = node.value*10+1;
            if (nv1<=b){
                queue.add(new Pair(nv1,node.count+1));
            }
            if (nv2<=b) {
                queue.add(new Pair(nv2, node.count+1));
            }
        }
        System.out.println(-1);
    }
}

class Pair{

    long value;
    int count;

    public Pair(long value, int count){
        this.value = value;
        this.count = count;
    }
}