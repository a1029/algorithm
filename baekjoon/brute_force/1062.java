package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static int n;
    public static int k;
    public static String[] words;
    public static boolean[] visit = new boolean[26];
    public static int result = 0;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        words = new String[n];

        if(k<5){
            System.out.println(0);
            return;
        }else if(k==26){
            System.out.println(n);
            return;
        }else{
            for(int i=0; i<n; i++) {
                String str = br.readLine();
                words[i] = str.substring(4, str.length() - 4);
            }
            k-=5;
            visit['a'-97]=true;
            visit['n'-97]=true;
            visit['t'-97]=true;
            visit['i'-97]=true;
            visit['c'-97]=true;
            dfs(0,0);
            System.out.println(result);
        }
    }

    public static void dfs(int start, int count){
        if(count==k){
            int tmp=0;
            for(int i=0; i<n; i++){
                boolean isTrue = true;
                for(int j=0; j<words[i].length(); j++){
                    if(!visit[words[i].charAt(j)-97]){
                        isTrue = false;
                        break;
                    }
                }
                if(isTrue){
                    tmp+=1;
                }
            }
            result = Math.max(result, tmp);
            return;
        }

        for(int i=start; i<26; i++){
            if(!visit[i]){
                visit[i] = true;
                dfs(i, count+1);
                visit[i] = false;
            }
        }
    }
}
