import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static ArrayList<Integer> arr = new ArrayList<>();
    public static ArrayList<Integer> input = new ArrayList<>();
    public static int max = 0;
    public static int n = 0;
    public static int m = 0;
    public static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            input.add(Integer.parseInt(st.nextToken()));
        }

        dfs(arr, 0);
        System.out.println(answer);
    }

    public static int dfs(ArrayList<Integer> arr, int index){

        if(arr.size()==3){
            int sum = arr.stream().mapToInt(Integer::intValue).sum();
            if(sum <= m && sum >= max){
                max = sum;
                answer = sum;
            }
            return 0;
        }

        for(int i=index; i<input.size(); i++){
            arr.add(input.get(i));
            dfs(arr, i + 1);
            arr.remove(input.get(i));
        }

        return 0;
    }
}
