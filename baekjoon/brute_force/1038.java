package brute_force;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        if (n>1022){
            System.out.println(-1);
        } else if(n<10){
            System.out.println(n);
        } else {
            Queue<Long> q = new LinkedList<>();
            int cnt = 0;
            for(int i=1; i<10; i++){
                q.add((long) i);
                cnt+=1;
            }
            while(cnt<n){
                long k = q.poll();
                long temp = k%10;
                for(int i=0; i<temp; i++){
                    q.add(k*10+i);
                    cnt+=1;
                    if(cnt==n){
                        System.out.println(k*10+i);
                        break;
                    }
                }
            }
        }
    }
}
