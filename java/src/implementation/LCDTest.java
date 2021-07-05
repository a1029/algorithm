package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class LCDTest {

    static int s;
    static String n;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        n = st.nextToken();

        for(int i=0; i<2*s+3; i++){
            for(int j=0; j<n.length(); j++){
                if (n.charAt(j)=='0'){
                    if (i==0 || i==2*s+3-1) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i==(2*s+3-1)/2){
                        IntStream.range(0, s+2).forEach(x -> System.out.print(" "));
                    } else {
                        System.out.print("|");
                        IntStream.range(0, s).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='1'){
                    if (i%((2*s+3-1)/2)==0) {
                        IntStream.range(0, s+2).forEach(x -> System.out.print(" "));
                    }
                    else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='2'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i<(2*s+3-1)/2) {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    } else {
                        System.out.print("|");
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                    }
                } else if(n.charAt(j)=='3'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='4'){
                    if (i==0 || i==2*s+3-1) {
                        IntStream.range(0, s+2).forEach(x -> System.out.print(" "));
                    } else if(i==(2*s+3-1)/2) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i<(2*s+3-1)/2) {
                        System.out.print("|");
                        IntStream.range(0, s).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    } else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='5'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i<(2*s+3-1)/2) {
                        System.out.print("|");
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                    } else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='6'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i<(2*s+3-1)/2) {
                        System.out.print("|");
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                    } else {
                        System.out.print("|");
                        IntStream.range(0, s).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='7'){
                    if (i==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i==(2*s+3-1)/2 || i==(2*s+3-1)) {
                        IntStream.range(0, s+2).forEach(x -> System.out.print(" "));
                    } else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='8'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else {
                        System.out.print("|");
                        IntStream.range(0, s).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                } else if(n.charAt(j)=='9'){
                    if (i%((2*s+3-1)/2)==0) {
                        System.out.print(" ");
                        IntStream.range(0, s).forEach(x -> System.out.print("-"));
                        System.out.print(" ");
                    } else if(i<(2*s+3-1)/2) {
                        System.out.print("|");
                        IntStream.range(0, s).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    } else {
                        IntStream.range(0, s+1).forEach(x -> System.out.print(" "));
                        System.out.print("|");
                    }
                }
                System.out.print(" ");
            }
            System.out.println("");
        }
    }
}
