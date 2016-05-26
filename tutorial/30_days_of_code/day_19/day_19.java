import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}

//Write your code here
class Calculator implements AdvancedArithmetic{
    public int divisorSum(int n){
        int output = 0;
        if (n == 1){
            output = 1;
        }
        else{
            for(int i = 1; i<=Math.pow(n, 0.5); i++){
                if (n%i == 0){
                    output += i;
                    output += (n/i);
                }
            }       
        }
        return output; 
    }
    
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
