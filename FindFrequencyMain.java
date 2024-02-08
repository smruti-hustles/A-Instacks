/******************************************************************************

                      Frequency of given character

*******************************************************************************/
import java.util.*;

public class FindFrequencyMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char t=sc.next().charAt(0);
        char r[]=s.toCharArray();
        int count=0;
        for (int i = 0; i < s.length(); i++) {
            char c = r[i];
            if (r[i]==t)
               count+=1;
            
        }
        System.out.println("frequency of "+t+" is =" + count);
    }
}
