//leap year
import java.util.*;
public class LeapYearMain{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int y=sc.nextInt();
        if((y%4==0 && y%100!=0)||(y%400==0))
         System.out.println(y+" is a leap yera");
        else
        System.out.println(y+" not is a leap yera");
    }
}
