import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char t[] = s.toCharArray();
        String r = "";
        for (int i = 0; i < s.length(); i++) {
            char c = t[i];
            if (c != 'a' && c != 'e' &&c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
                r += c;
            }
        }
        System.out.println("String after removing vowels =" + r);
    }
}
