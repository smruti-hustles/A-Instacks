/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class AnagramsMain
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
	    String t=sc.nextLine();
	    if(s.length()!=t.length()){
	        System.out.println("not anagrams");
	    }
	    else{
	        char p[]=s.toCharArray();
	        char q[]=s.toCharArray();
	        Arrays.sort(p);
	        Arrays.sort(q);
	       
	        if(Arrays.equals(p,q))
	            System.out.println("anagrams");
	        else
	        System.out.println("not anagrams");
	    }
	}
}
