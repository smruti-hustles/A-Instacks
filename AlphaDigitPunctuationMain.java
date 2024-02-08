import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        char t[]=s.toCharArray();
        String r="";
        for(int i=0;i<t.length;i++){
            char c=t[i];
            if(Character.isDigit(c))
              System.out.println(c + " is digit");
            else if(Character.isAlphabetic(c))  
              System.out.println(c + " is alphabet");
            else
              System.out.println(c + " is punctuation mark");
        }
    }
}
