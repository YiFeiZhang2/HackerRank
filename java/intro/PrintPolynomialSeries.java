import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class PrintPolynomialSeries{

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int numCases = in.nextInt();
        for(int i = 0; i<numCases; i++){
            int constant = in.nextInt();
            int coeff = in.nextInt();
            int limit = in.nextInt();
            
            int output = constant;
            for(int j = 0; j < limit; j++){
                output += (int)Math.pow(2,j)*coeff;
                System.out.print(output + " ");
            }
            System.out.println();
        }
    }
}
