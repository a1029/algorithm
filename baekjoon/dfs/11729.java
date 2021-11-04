import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int n = 0;
    public static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        hanoi(n, 1,2,3);
        System.out.println((int)Math.pow(2, n) - 1);
        System.out.println(sb);
    }

    public static void hanoi(int n, int from, int mid, int to){

        if(n==1){
            sb.append(from + " " + to + "\n");
            return;
        }
        hanoi(n-1, from, to ,mid);
        sb.append(from + " " + to + "\n");
        hanoi(n-1, mid, from, to);
    }
}
