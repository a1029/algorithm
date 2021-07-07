package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 시그널 {

    static int n;
    static String signal;
    static char[][] map;
    static StringBuilder result = new StringBuilder();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        signal = br.readLine();

        map = new char[5][n/5];

        int index = 0;
        for (int i=0; i<5; i++){
            for (int j=0; j<n/5; j++){
                map[i][j] = signal.charAt(index);
                index+=1;
            }
        }

        int j=0;
        while (j<n/5){
            if (map[0][j]=='.'){
                j+=1;
                continue;
            }
            int count = 0;
            if (j==n/5-1){
                count = 5;
            } else {
                for (int i=0; i<5; i++){
                    if(map[i][j+1]=='.'){
                        count+=1;
                    }
                }
            }
            if (count==5){
                result.append("1");
                j += 1;
            } else {
                result.append(checkNum(j));
                j += 3;
            }
        }
        System.out.println(result);
    }

    static int checkNum(int idx){

        if (map[1][idx+1]=='.' && map[2][idx+1]=='.' && map[3][idx+1]=='.' && map[4][idx+1]=='#'){
            return 0;
        } else if (map[1][idx]=='.' && map[3][idx+2]=='.'){
            return 2;
        } else if (map[1][idx]=='.' && map[2][idx]=='#' && map[3][idx]=='.'){
            return 3;
        } else if (map[0][idx]=='#' && map[0][idx+1]=='.'){
            return 4;
        } else if (map[1][idx+2]=='.' && map[3][idx]=='.'){
            return 5;
        } else if (map[1][idx+2]=='.' && map[3][idx]=='#'){
            return 6;
        } else if (map[2][idx]=='.'){
            return 7;
        } else if (map[3][idx]=='#'){
            return 8;
        } else {
            return 9;
        }
    }
}
