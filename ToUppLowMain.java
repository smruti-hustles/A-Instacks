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
	    int l=s.length();
	    String res1=" ";
	    String res2=" ";
	 char p[]=s.toCharArray();
	 char q[]=s.toCharArray();
	    System.out.println(s); 
	    for(int i=0;i<l;i++){
	        if(Character.isAlphabetic(p[i]))
	        res1+=Character.toLowerCase(p[i]);
	        else
	        res1+=p[i];
	    }
	     System.out.println(res1);
	      for(int i=0;i<l;i++){
	        if(Character.isAlphabetic(q[i]))
	        res2+=Character.toUpperCase(q[i]);
	        else
	        res2+=q[i];
	        
	    }
	     System.out.println(res1);
	        
           
	}
}
