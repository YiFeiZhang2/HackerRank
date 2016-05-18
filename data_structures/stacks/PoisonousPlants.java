import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class PoisonousPlants{
	public static void main(String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner in = new Scanner(System.in);
    int numPlants = Integer.parseInt(in.nextLine());
    int[] pesticideArray = new int[numPlants];
    for(int i = 0; i<numPlants; i++){
    	pesticideArray[i] = in.nextInt();
    }
    int[] killerArray = getKillerArray(pesticideArray, numPlants);
    System.out.println(Arrays.toString(killerArray));    
    
	}
	
	static int[] getKillerArray(int[] pesticideArray, int numPlants){
        int[] killerArray = new int[numPlants];
        killerArray[0] = -1;
        int maxDay = 0;
        
        Stack<Integer>s = new Stack<Integer>();
        s.push(0);
        
        for(int i = 1; i<numPlants; i++){
            maxDay = 1;
        	
            while(!s.isEmpty() && pesticideArray[i]<pesticideArray[s.peek()]){
                s.pop();
                maxDay += 1;
            }
            
            killerArray[i] = s.peek();
            
            s.push(i);
        }
        System.out.println(maxDay);
        return killerArray;
    }
}