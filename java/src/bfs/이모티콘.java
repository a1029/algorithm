package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class 이모티콘 {

    static int s = 0;
    static Queue<Emotion> queue = new LinkedList<>();
    static boolean[][] visit = new boolean[1001][1001];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Integer.parseInt(br.readLine());

        queue.add(new Emotion(0,1,0));
        visit[0][1] = true;

        while(!queue.isEmpty()){
            Emotion emo = queue.poll();
            if (emo.screen==s){
                System.out.println(emo.second);
                break;
            } else {
                queue.add(new Emotion(emo.screen, emo.screen, emo.second+1));

                if(emo.clipboard!=0 && emo.screen + emo.clipboard <= s && !visit[emo.clipboard][emo.screen+emo.clipboard]){
                    queue.add(new Emotion(emo.clipboard, emo.screen+emo.clipboard, emo.second+1));
                    visit[emo.clipboard][emo.screen+emo.clipboard] = true;
                }

                if(emo.screen>=1 && !visit[emo.clipboard][emo.screen-1]){
                    queue.add(new Emotion(emo.clipboard, emo.screen-1, emo.second+1));
                    visit[emo.clipboard][emo.screen-1] = true;
                }
            }
        }
    }
}

class Emotion{

    int clipboard;
    int screen;
    int second;

    public Emotion(int clipboard, int screen, int second){
        this.clipboard = clipboard;
        this.screen = screen;
        this.second = second;
    }
}
