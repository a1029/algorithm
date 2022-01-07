import java.util.Arrays;

class Solution {
    
    public static boolean[] visit;
    public static int answer = Integer.MAX_VALUE;
    
    public static void dfs(String now, int count, String target, String[] words) {
        if (now.equals(target)) {
            answer = Math.min(answer, count);
            return;
        }

        for (int i=0; i<words.length; i++) {
            if (!visit[i] && check(now, words[i])) {
                visit[i] = true;
                dfs(words[i], count+1, target, words);
                visit[i] = false;
            }
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        visit = new boolean[words.length];
        Arrays.fill(visit, false);

        for(int i=0; i<words.length; i++) {
            dfs(begin, 0, target, words);
        }
        
        if (answer==Integer.MAX_VALUE) {
            return 0;
        }
        return answer;
    }
    
    public static boolean check(String a, String b) {
        int count = 0;
        for (int i=0; i<a.length(); i++) {
            if (a.charAt(i)==b.charAt(i)) {
                count += 1;
            }
        }
        return count == a.length() - 1;
    }
}