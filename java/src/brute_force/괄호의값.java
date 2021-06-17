package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 괄호의값 {

    public static Stack<Character> stack = new Stack<>();
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static String str = "";
    public static int val = 1;
    public static int result = 0;
    public static int flag = 0;
    public static void main(String[] args) throws IOException {

        str = br.readLine();
        for (int i = 0; i<str.length(); i++) {
            if (str.charAt(i)=='(') {
                stack.add(str.charAt(i));
                val *= 2;
            }
            if (str.charAt(i)=='[') {
                stack.add(str.charAt(i));
                val *= 3;
            }
            if (str.charAt(i)==')') {
                if (stack.empty() || stack.peek()!='(') {
                    flag = 1;
                    break;
                }
                if (str.charAt(i-1)=='(') {
                    result += val;
                }
                stack.pop();
                val /= 2;
            }
            if (str.charAt(i)==']') {
                if (stack.empty() || stack.peek()!='[') {
                    flag = 1;
                    break;
                }
                if (str.charAt(i-1)=='[') {
                    result += val;
                }
                stack.pop();
                val /= 3;
            }
        }
        if(flag==1 || !stack.empty()){
            System.out.println(0);
        }else{
            System.out.println(result);
        }
    }
}
