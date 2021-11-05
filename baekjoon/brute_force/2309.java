package brute_force;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

    public static ArrayList<ArrayList<Integer>> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = 9;
        int r = 7;
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        boolean[] visited = new boolean[n];
        combination(arr, visited, 0, n, r);

        Collections.sort(result.get(0));
        for(int i=0; i<7; i++){
            System.out.println(result.get(0).get(i));
        }
    }

    static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }
        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }

    static void print(int[] arr, boolean[] visited, int n) {
        ArrayList<Integer> tmp = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                tmp.add(arr[i]);
            }
        }

        int sum = tmp.stream().mapToInt(Integer::intValue).sum();
        if (sum==100){
            result.add(tmp);
        }
    }
}
