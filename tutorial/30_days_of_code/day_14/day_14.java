import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
  	private int[] elements;
  	public int maximumDifference;

	Difference(int[] a){
        	this.elements = a;
    	}

    	void computeDifference(){
        	Arrays.sort(this.elements);
        	maximumDifference = Math.abs(this.elements[this.elements.length-1] - this.elements[0]);
    	}

} // End of Difference Class

class Solution {        
  	public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int N = sc.nextInt();
    	int[] a = new int[N];
    
    	for (int i = 0; i < N; i++) {
    		a[i] = sc.nextInt();
    	}

      	Difference D = new Difference(a);

        D.computeDifference();

        System.out.print(D.maximumDifference);
   }
}	
