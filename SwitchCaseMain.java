import java.util.*;
public class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        boolean b=true;
        while(b){
            System.out.println("Enter number ");
        int n=sc.nextInt();
         System.out.println("1. sum of odd numbers\n 2. sum of even numbers");
        int ch=sc.nextInt();
        
        switch(ch){
            case 1:int o=0;
                    for(int i=1;i<=n;i+=2){
                      o+=i;
                    }
                    System.out.println("sum of odd numbers = "+o);
                break;
            case 2:int e=0;
                    for(int i=2;i<=n;i+=2){
                      e+=i;
                    }
                    System.out.println("sum of even numbers = "+e);
                break;
            default: System.out.println("Invalid choice");    
        }
        System.out.println("Dou you want to repeat ? true or false");
        b=sc.nextBoolean();
        
        }
       
    }
}
