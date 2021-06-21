import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 11404. 플로이드
public class 플로이드 {

    static final int INF = (int)1e9;
    static int n, m;
    static int[][] graph;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws Exception{

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        graph = new int[n+1][n+1];
        for(int i=0; i<n+1; i++){
            for(int j=0; j<n+1; j++){
                graph[i][j] = INF;
            }
        }
        for(int i=0; i<m; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a][b] = Math.min(graph[a][b], c);
        }

        for(int i=1; i<n+1; i++){
            graph[i][i] = 0;
        }


        for (int k=1; k<n+1; k++){
            for(int i=1; i<n+1; i++){
                for(int j=1; j<n+1; j++){
                    graph[i][j] = Math.min(graph[i][j], graph[i][k]+graph[k][j]);
                }
            }
        }

        for (int i=1; i<n+1; i++){
            for(int j=1; j<n+1; j++){
                if(graph[i][j]==INF){
                    System.out.print(0 + " ");
                }else{
                    System.out.print(graph[i][j] + " ");
                }
            }
            System.out.println("");
        }
    }
}