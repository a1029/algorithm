//package String;
//
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.StringTokenizer;
//
//public class Strfry {
//
//    static ArrayList<String[]> result = new ArrayList<>();
//    static void permutation(String[] arr, int depth, int n, int r) {
//        if (depth == r) {
//            result.add(arr);
//            return;
//        }
//
//        for (int i=depth; i<n; i++) {
//            swap(arr, depth, i);
//            permutation(arr, depth + 1, n, r);
//            swap(arr, depth, i);
//        }
//
//    }
//
//    static void swap(String[] arr, int depth, int i) {
//        String temp = arr[depth];
//        arr[depth] = arr[i];
//        arr[i] = temp;
//    }
//
//    public static void main(String[] args) throws IOException {
//
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        int tc = Integer.parseInt(br.readLine());
//        while(tc-->0){
//            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
//            String[] a = st.nextToken().split("");
//            String b = st.nextToken();
//            permutation(a, a.length, a.length, a.length);
//            for(int i=0; i<result.size(); i++){
//                System.out.println(Arrays.toString(result.get(i)));
//            }
//        }
//    }
//}
