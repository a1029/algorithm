package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        while(tc-->0){
            String command = br.readLine();
            int x=0,y=0;
            int up=0,down=0,left=0,right=0;
            int d = 3;
            for(int i=0; i<command.length(); i++){
                if(command.charAt(i)=='F'){
                    x+=dx[d];
                    y+=dy[d];
                } else if(command.charAt(i)=='B'){
                    x-=dx[d];
                    y-=dy[d];
                } else if(command.charAt(i)=='L'){
                    d -= 1;
                    if (d==-1) d=3;
                } else {
                    d += 1;
                    if (d==4) d=0;
                }
                right = Math.max(right, y);
                left = Math.min(left, y);
                down = Math.max(down, x);
                up = Math.min(up, x);
            }
            System.out.println(Math.abs(up-down)*Math.abs(right-left));
        }
    }
}
