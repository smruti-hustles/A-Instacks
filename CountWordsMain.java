/******************************************************************************

Count number of words in a string or text

*******************************************************************************/
import java.util.*;
public class CountWordsMain
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
	    String t[]=s.split(" ");
	    System.out.println("No of words = " + t.length);
	}
}
