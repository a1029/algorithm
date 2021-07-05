package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.IntStream;

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
            int count = 0;
            for (int i=0; i<5; i++){
               if(map[i][j+1]=='.'){
                   count+=1;
               }
            }
            if (count==5){
                result.append("1");
                j+=2;
            } else {
                int num = checkNum(j);
                result.append(num);
                j+=4;
            }
        }
        System.out.println(result);
    }

    static int checkNum(int index){

        int count = 0;
        for(int j=index; j<index+3; j++){
            if(map[0][j]=='#'){
                count+=1;
            }
            if(map[4][j]=='#'){
                count+=1;
            }
        }
        // 0,2,3,5,6,8,9
        if (count==6){
            if (map[1][index+1]=='.' && map[2][index+1]=='.' && map[1][index+1]=='.') {
                return 0;
            } else if(map[1][index]=='.' && map[3][index+2]=='.'){
                return 2;
            } else if(map[1][index]=='.' && map[3][index]=='.'){
                return 3;
            } else if(map[1][index+2]=='.' && map[3][index]=='.'){
                return 5;
            } else if(map[1][index+2]=='.' && map[3][index]=='#'){
                return 6;
            } else if(map[1][index+1]=='.' && map[2][index+1]=='#' && map[3][index+1]=='.'){
                return 8;
            } else{
                return 9;
            }
        // 4, 7
        } else {
            if (map[2][index+1]=='#'){
                return 4;
            } else {
                return 7;
            }
        }
    }

}
