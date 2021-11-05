package implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static ArrayList<String> result = new ArrayList<>();
    static String commonType;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        commonType = st.nextToken();
        while(st.hasMoreTokens()){
            String str = st.nextToken();
            StringBuilder name = new StringBuilder();
            StringBuilder type = new StringBuilder();
            for(int i=0; i<str.length()-1; i++){
                if (Character.isAlphabetic(str.charAt(i))){
                    name.append(str.charAt(i));
                } else {
                    if (str.charAt(i)==']'){
                        type.append('[');
                    }else if(str.charAt(i)=='['){
                        type.append(']');
                    } else {
                        type.append(str.charAt(i));
                    }
                }
            }
            result.add(commonType + new StringBuffer(type).reverse() + " " + name + ";");
        }
        result.forEach(System.out::println);
    }
}
