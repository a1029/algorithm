package implementation;

import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.BufferedReader;

// 1756
public class 피자굽기{
    
    public static int d,n;
    public static int[] oven;
    public static int[] pizza;
    public static int[] visit;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        d = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        oven = new int[d];
        pizza = new int[n];
        visit = new int[d];
        st = new StringTokenizer(br.readLine());
		for(int i = 0; i < d; i++) {
			oven[i] = Integer.parseInt(st.nextToken());
			if(i > 0 && oven[i-1] < oven[i]) {
				oven[i] = oven[i-1];
			}
		}
        st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			pizza[i] = Integer.parseInt(st.nextToken());
		}

        int idx = 0;
        for(int i=d-1; i>-1; i--){
            if(pizza[idx]<=oven[i]){
                visit[idx] = 1+i;
                idx++;
            }
            if(idx==n){
                break;
            }
        }

        if(idx==n){
            System.out.println(visit[idx-1]);
        }else{
            System.out.println(0);
        }
    }
}