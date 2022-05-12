package leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class q22 {

    ArrayList<String> answer = new ArrayList<>();
    int left = 0;
    int right = 0;

    public List<String> generateParenthesis(int n) {
        left = n;
        right = n;
        dfs("", n);

        return answer;
    }

    public void dfs(String str, int n) {

        if (str.length() == n*2 && check(str)) {
            answer.add(str);
            return;
        }

        if (left > 0) {
            left -= 1;
            dfs(str + "(", n);
            left += 1;
        }

        if (right > 0) {
            right -= 1;
            dfs(str + ")", n);
            right += 1;
        }
    }

    public boolean check(String str) {
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<str.length(); i++) {
            if (str.charAt(i) == '(') {
                stack.add(str.charAt(i));
            } else {
                if (stack.isEmpty() || stack.peek() == ')') {
                    return false;
                }
                stack.pop();
            }
        }

        return true;
    }

    /**
     * solution2
     */
    public List<String> generateParenthesis2(int n) {

        dfs2("", 0, 0, n);
        return answer;
    }

    public void dfs2(String str, int open, int close, int n) {

        if (str.length() == n*2) {
            answer.add(str);
            return;
        }

        if (open < n) {
            dfs2(str+"(", open+1, close, n);
        }

        if (close < open) {
            dfs2(str+")", open, close+1, n);
        }
    }

    public static void main(String[] args) {
        q22 q = new q22();
        System.out.println(q.generateParenthesis(2));
        System.out.println(q.generateParenthesis2(2));
    }

}
