/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
	    String p=sc.nextLine();
	    int lens=s.length();
	    int lenp=p.length();
	    int red=0;
	    
	    for(int i=0;i<=lens-lenp;i++){
	        String t=s.substring(i,i+lenp);
	        if(t.equals(p))
	        red=red+1;
	    }
	    
	    if (red>0)
            System.out.println("present");
        else
            System.out.println("Not present");
	}
}
