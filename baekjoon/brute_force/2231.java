import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int i=1; i<=n; i++){
            int constructor = cal(i);
            if(constructor==n){
                System.out.println(i);
                return;
            }
        }
        System.out.println(0);
    }

    public static int cal(int val){

        int sum = val;
        String str = String.valueOf(val);
        for(int i=0; i<str.length(); i++){
            sum += Integer.parseInt(String.valueOf(str.charAt(i)));
        }

        return sum;
    }


}
