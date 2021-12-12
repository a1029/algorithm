package 카카오_2021_채용연계형_인턴쉽;

import java.util.Stack;

public class 표편집 {

    public static void main(String[] args) {

        System.out.println(solution(10,1,new String[]{"C","C","C","Z","Z"}));
        System.out.println(solution(8, 2,new String[]{"D 2","C","U 3","C","D 4","C","U 2","Z","Z"}));
        System.out.println(solution(8, 2,new String[]{"D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"}));

    }

    public static class Node{
        int prev, cur, next;

        public Node(int prev, int cur, int next) {
            this.prev = prev;
            this.cur = cur;
            this.next = next;
        }
    }

    public static String solution(int n, int k, String[] cmd) {

        int[] prev = new int[n];
        int[] next = new int[n];
        for(int i=0; i<n; i++) {
            prev[i] = i-1;
            next[i] = i+1;
        }
        next[n-1] = -1;

        Stack<Node> stack = new Stack<>();
        StringBuilder sb = new StringBuilder("O".repeat(n));

        for(int i=0; i<cmd.length; i++) {
            char c = cmd[i].charAt(0);
            if(c=='U') {
                int index = Integer.parseInt(cmd[i].substring(2));
                while(index-->0) {
                    k = prev[k];
                }
            } else if(c=='D') {
                int index = Integer.parseInt(cmd[i].substring(2));
                while(index-->0) {
                    k = next[k];
                }
            } else if(c=='C') {
                stack.push(new Node(prev[k], k, next[k]));
                if(prev[k]!=-1){
                    next[prev[k]] = next[k];
                }
                if(next[k]!=-1){
                    prev[next[k]] = prev[k];
                }
                sb.setCharAt(k, 'X');
                if(next[k]!=-1){
                    k = next[k];
                } else {
                    k = prev[k];
                }
            } else {
                Node node = stack.pop();
                if(node.prev!=-1) {
                    next[node.prev] = node.cur;
                }
                if(node.next!=-1) {
                    prev[node.next] = node.cur;
                }
                sb.setCharAt(node.cur, 'O');
            }
        }
        return sb.toString();
    }

}
