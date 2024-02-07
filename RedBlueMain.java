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
	    int red=0;
	    int blue=0;
	    for(int i=0;i<=s.length()-3;i++){
	        String t=s.substring(i,i+3);
	        if(t.equals("red"))
	        red=red+1;
	    }
	    for(int i=0;i<=s.length()-4;i++){
	        String t=s.substring(i,i+4);
	        if(t.equals("blue"))
	        blue=blue+1;
	    }
	    System.out.println(red);
	    System.out.println(blue);
	    if (red == blue)
            System.out.println("The appearance of red and blue are the same");
        else
            System.out.println("The appearance of red and blue are not the same");
	}
}
