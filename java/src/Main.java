import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 12865. 평범한 배낭
public class Main {
    

    static int n, k;
    static int[] weight;
    static int[] value;
    static int[][] dp;
    public static void main(String[] args) throws Exception{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        weight = new int[n+1];
        value = new int[n+1];
        dp = new int[n+1][k+1];

        for(int i=1; i<n+1; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            weight[i] = a;
            value[i] = b;
        }

        for(int i=1; i<n+1; i++){
            for(int j=1; j<k+1; j++){
                if(j<weight[i]){
                    dp[i][j] = dp[i-1][j];
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
                }
            }
        }

        System.out.println(dp[n][k]);


    }
}
