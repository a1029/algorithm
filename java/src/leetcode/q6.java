package leetcode;

import java.util.ArrayList;
import java.util.Stack;

public class q6 {
    public String convert(String s, int numRows) {
        ArrayList<Stack<String>> arr = new ArrayList<>();
        for(int i=0; i<numRows; i++) {
            arr.add(new Stack<>());
        }

        int pos = 0;
        String flag = "";
        for(int i=0; i<s.length(); i++) {
            if (pos == 0) {
                flag = "down";
            } else if (pos == numRows - 1) {
                flag = "up";
            }
            arr.get(pos).add(s.substring(i, i+1));

            if (numRows == 1) {
                continue;
            }
            pos = flag.equals("down") ? pos + 1 : pos - 1;
        }

        StringBuilder answer = new StringBuilder();
        arr.forEach(stack -> {
            answer.append(String.join("", stack));
        });

        return answer.toString();
    }

    public String convert2(String s, int numRows) {
        StringBuilder[] sb = new StringBuilder[numRows];
        for(int i=0; i<numRows; i++) {
            sb[i] = new StringBuilder();
        }

        int len = s.length();
        int pos = 0;
        while (pos < len) {
            for (int i=0; i<numRows && pos<len; i++) {
                sb[i].append(s.charAt(pos++));
            }
            for (int i=numRows-2; i>=1 && pos<len; i--) {
                sb[i].append(s.charAt(pos++));
            }
        }

        return String.join("", sb);
    }

    public static void main(String[] args) {
        q6 q = new q6();
        System.out.println(q.convert("AB", 1));
        System.out.println(q.convert2("PAYPALISHIRING", 3));
    }
}
