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
	    String res=" ";
	 char p[]=s.toCharArray();
	    
	    for(int i=0;i<l;i++){
	        if(Character.isUpperCase(p[i]))
	        res+=Character.toLowerCase(p[i]);
	        
	        else if(Character.isLowerCase(p[i])){
	        res+=Character.toUpperCase(p[i]);
	         }
	         else{
	             res+=p[i];
	         }
	    }
            System.out.print(s);
            System.out.print(res);
	}
}
