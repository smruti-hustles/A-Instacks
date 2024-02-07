/******************************************************************************

Count number of vowels and consonants

*******************************************************************************/
import java.util.*;
public class VowelConsonantsMain
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String s=sc.nextLine();
	    int l=s.length();
	    int v=0;
	    int con=0;
	   
	 char p[]=s.toCharArray();
	
	    for(int i=0;i<l;i++){
	        char c=p[i];
	        if(Character.isAlphabetic(c)){
	        if(c=='a'||c=='e'||i=='o'||i=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U')
	        v+=1;
	        else
	        con+=1;
	        }
	      }
	      
	     System.out.println("No of Vowels = "+v);
	     System.out.println("No of consonants = "+con);
	}
}
