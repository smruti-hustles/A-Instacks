/******************************************************************************

Finding no of  ocuurances of substring

*******************************************************************************/
import java.util.*;
public class OccurancesMain
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
	    String p=sc.nextLine();
	    int lens=s.length();
	    int lenp=p.length();
	    int count=0;
	    
	    for(int i=0;i<=lens-lenp;i++){
	        String t=s.substring(i,i+lenp);
	        if(t.equals(p))
	        count=count+1;
	    }
	    
	    if (count>0){
            System.out.println("It is a substring");
            System.out.println("No of occurances of "+p+" are : "+count);
	    }
        else
            System.out.println("It is not a substring");
	}
}
