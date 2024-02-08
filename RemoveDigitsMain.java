import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        char t[]=s.toCharArray();
        String r="";
        for(int i=0;i<t.length;i++){
            char c=t[i];
            if(!Character.isDigit(c))
            r+=c;
        }
        System.out.println(r);
    }
}
