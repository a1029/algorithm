package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[][] matches;
    static boolean isEndGame = false;
    static final int TEAM_COUNT = 6;
    static final int MATCH_COUNT = 15;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int tc = 4;

        matches = new int[MATCH_COUNT][2];

        int index = 0;
        for(int i=0; i<TEAM_COUNT-1; i++){
            for(int j=i+1; j<TEAM_COUNT; j++){
                matches[index][0] = i;
                matches[index][1] = j;
                index+=1;
            }
        }

        while(tc-->0){
            st = new StringTokenizer(br.readLine());
            int[][] worldCup = new int[TEAM_COUNT][3];
            boolean isPossible = true;

            for(int i=0; i<TEAM_COUNT; i++){
                int win = Integer.parseInt(st.nextToken());
                int draw = Integer.parseInt(st.nextToken());
                int lose = Integer.parseInt(st.nextToken());

                worldCup[i][0] = win;
                worldCup[i][1] = draw;
                worldCup[i][2] = lose;

                if(win+draw+lose!=5){
                    isPossible = false;
                    break;
                }
            }

            if(isPossible){
                backTracking(worldCup, 0);
                if(isEndGame){
                    sb.append(1);
                } else {
                    sb.append(0);
                }
            } else {
                sb.append(0);
            }

            sb.append(" ");
            isEndGame = false;
        }
        System.out.print(sb);
    }

    static void backTracking(int[][] worldCup, int matchCount){
        if(matchCount==MATCH_COUNT){
            isEndGame = true;
            return;
        }

        int aTeam = matches[matchCount][0];
        int bTeam = matches[matchCount][1];

        if(worldCup[aTeam][0] > 0 && worldCup[bTeam][2] > 0){
            worldCup[aTeam][0]-=1;
            worldCup[bTeam][2]-=1;
            backTracking(worldCup, matchCount+1);
            worldCup[aTeam][0]+=1;
            worldCup[bTeam][2]+=1;
        }

        if(worldCup[aTeam][1] > 0 && worldCup[bTeam][1] > 0){
            worldCup[aTeam][1]-=1;
            worldCup[bTeam][1]-=1;
            backTracking(worldCup, matchCount+1);
            worldCup[aTeam][1]+=1;
            worldCup[bTeam][1]+=1;
        }

        if(worldCup[aTeam][2] > 0 && worldCup[bTeam][0] > 0){
            worldCup[aTeam][2]-=1;
            worldCup[bTeam][0]-=1;
            backTracking(worldCup, matchCount+1);
            worldCup[aTeam][2]+=1;
            worldCup[bTeam][0]+=1;
        }
    }
}
