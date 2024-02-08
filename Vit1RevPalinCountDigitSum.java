/*
Write a program to find reverse of a given number, count of digits, sum of individual digits, print palindrome or not
*/
import java.util.*;
public class Vit1RevPalinCountDigitSum{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int r,rev=0, sum=0;
        int t=n;
        while(n>0){
            r=n%10;
            rev=rev*10+r;
            sum=sum+r;
            n=n/10;
        }
        System.out.println("The number is = "+t);
        System.out.println("Reverse of the number is = "+rev);
        if(t==rev)
        System.out.println("palindrome");
        else
        System.out.println("Not palindrome");
        
        System.out.println("Sum of digits is = "+sum);
        
        String s=Integer.toString(t);
        System.out.println("count of digits is = "+s.length());
    }
}
