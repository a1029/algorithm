import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 15684. 사다리 조작
public class ladder{

    static int n,m,h;
    static int[][] ladder;
    static int need = 0;
    static int flag = 0;

    public static void dfs(int col, int ladderCnt){

        if(flag==1){
           return; 
        }

        if (ladderCnt==need){
            int possible = 1;
            for(int i=1; i<n+1; i++){
                int row = i;
                for(int j=1; j<h+1; j++){
                    if (ladder[j][row]==1){
                        row++;
                    }
                    else if(row>1 && ladder[j][row-1]==1){
                        row--;
                    }
                }
                if(i!=row){
                    possible = 0;
                    break;
                }
            }
            if(possible==1){
                flag=1;
            }
            return;
        }

        for(int i=col; i<h+1; i++){
            for(int j=1; j<n; j++){
                if (ladder[i][j-1] == 0 && ladder[i][j] == 0 && ladder[i][j+1] == 0){
                    ladder[i][j] = 1;
                    dfs(i, ladderCnt+1);
                    ladder[i][j] = 0;
                }
            }
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        ladder = new int[h+1][n+1];

        for (int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine(), " ");
            ladder[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 1;
        }
    
        for(int i=0; i<4; i++){
            need = i;
            dfs(0, 0);
            if(flag==1){
                System.out.println(need);
                return;
            }
        }
        System.out.println("-1");
        return;
    }
}