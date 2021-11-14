class Solution {
    
    public static int answer = 0;
    public static int count = 0;
    
    public int solution(String word) {
        dfs("", "AEIOU", word);
        return answer;
    }
    
    public static void dfs(String curr, String order, String word){

        if(curr.equals(word)){
            answer = count;
            return;
        }

        if(curr.length()==5){
            return;
        }

        for(int i=0; i<order.length(); i++){
            count += 1;
            dfs(curr + order.charAt(i), order, word);
        }
    }
}
