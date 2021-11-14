import java.util.HashSet;

class Solution {
    
    public static int answer = -1;
    public static HashSet<Integer> visit = new HashSet<>();
    
    public int solution(int k, int[][] dungeons) {
        dfs(k, 0, dungeons);
        return answer;
    }
    
    public static void dfs(int k, int count, int[][] dungeons){

        for(int i=0; i<dungeons.length; i++){
            if(!visit.contains(i) && k>=dungeons[i][0]){
                visit.add(i);
                dfs(k-dungeons[i][1], count+1, dungeons);
                visit.remove(i);
            }
        }
        answer = Math.max(answer, count);
    }
}