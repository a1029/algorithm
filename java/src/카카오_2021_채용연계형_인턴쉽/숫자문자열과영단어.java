package 카카오_2021_채용연계형_인턴쉽;

public class 숫자문자열과영단어 {

    public static void main(String[] args) {

        System.out.println(solution("23foursix5sixsix7"));
    }

    public static int solution(String s) {

        s = s
                .replaceAll("one", "1")
                .replaceAll("two", "2")
                .replaceAll("three", "3")
                .replaceAll("four", "4")
                .replaceAll("five", "5")
                .replaceAll("six", "6")
                .replaceAll("seven", "7")
                .replaceAll("eight", "8")
                .replaceAll("nine", "9");
        return Integer.parseInt(s);
    }

}
