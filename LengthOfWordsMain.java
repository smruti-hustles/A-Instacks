// Length of each word in the string
import java.util.*;
public class LengthOfWordsMain{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String t[]=s.split(" ");
        for(int i=0;i<t.length;i++){
            System.out.println("length of "+t[i]+" is = "+t[i].length());
        }
    }
}
