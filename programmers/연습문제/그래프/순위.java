import java.util.Arrays;

class Solution {

    public static void main(String[] args) {
        solution(5, new int[][]{{4,3},{4,2},{3,2},{1,2},{2,5}});
        solution(5, new int[][]{{1,4},{4,2},{2,5},{5,3}});
    }

    public static int solution(int n, int[][] results) {
        int answer = 0;

        int[][] graph = new int[n][n];
        for(int[] row: graph) {
            Arrays.fill(row, -1);
        }

        for(int i=0; i<results.length; i++) {
            graph[results[i][0]-1][results[i][1]-1] = 1;
            graph[results[i][1]-1][results[i][0]-1] = 0;
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                for(int k=0; k<n; k++) {
                    if (graph[j][i]==1 && graph[i][k]==1) {
                        graph[j][k] = 1;
                        graph[k][j] = 0;
                    }
                }
            }
        }
        for(int i=0; i<n; i++) {
            int count = 0;
            for(int j=0; j<n; j++) {
                if (i!=j && graph[i][j]!=-1 && graph[j][i] !=-1) {
                    count += 1;
                }
            }
            if (count==n-1) {
                answer += 1;
            }
        }
        return answer;
    }
}