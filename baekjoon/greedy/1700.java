package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] order = new int[k];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<k; i++) {
            order[i] = Integer.parseInt(st.nextToken());
        }
        boolean[] use = new boolean[101];
        int put = 0;
        int result = 0;
        for(int i=0; i<k; i++){
            int now = order[i];

            if(!use[now]){
                if(put<n){
                    use[now] = true;
                    put+=1;
                }else{
                    ArrayList<Integer> list = new ArrayList<>();
                    for(int j=i; j<k; j++){
                        if(use[order[j]] && !list.contains(order[j])){
                            list.add(order[j]);
                        }
                    }
                    if(list.size()!=n){
                        for(int j=0; j<use.length; j++){
                            if(use[j] && !list.contains(j)){
                                use[j]=false;
                                break;
                            }
                        }
                    } else {
                        int last = list.get(list.size()-1);
                        use[last] = false;
                    }
                    use[now] = true;
                    result+=1;
                }
            }
        }
        System.out.println(result);
    }
}
