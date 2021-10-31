package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.util.StringTokenizer;

public class 빗물 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        ArrayList<Integer> height = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<w; i++){
            height.add(Integer.parseInt(st.nextToken()));
        }

        /*if (height.isEmpty()){
            System.out.println(0);
            return;
        }

        int result = 0;
        int left=0, right=height.size()-1;
        int left_max=height.get(left), right_max=height.get(right);

        while (left<right){
            left_max = Math.max(height.get(left),left_max);
            right_max = Math.max(height.get(right),right_max);

            if (left_max<=right_max){
                result += left_max-height.get(left);
                left += 1;
            }else{
                result += right_max-height.get(right);
                right -= 1;
            }
        }
        System.out.println(result);
        */

        Stack<Integer> stack = new Stack<>();

        int result = 0;
        for(int i=0; i<height.size(); i++){
            while(!stack.empty() && height.get(i) > height.get(stack.peek())){
                int top = stack.pop();

                if (stack.empty()){
                    break;
                }

                int dist = i - stack.peek() - 1;
                int differ = Math.min(height.get(i), height.get(stack.peek())) - height.get(top);

                result += dist * differ;
            }
            stack.push(i);
        }
        System.out.println(result);
    }
}
