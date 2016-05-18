import java.io.*;
import java.util.*;

public class Java1DArrayPart1 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int length = in.nextInt();
        int[] intArray = new int[length];
        int numNeg = 0;
        int total = 0;
        
        for(int i = 0; i<length; i++){
            intArray[i] = in.nextInt();
        }

        for(int i = 1; i<=length; i++){
            for(int j = 0; j<=length-i; j++){
                int[] subArray = java.util.Arrays.copyOfRange(intArray, j, j+i);
                total = 0;
                for(int number : subArray){
                    total += number;
                }
                if(total < 0){
                    numNeg ++;
                }
            }
        }
        
        System.out.println(numNeg);
        
    }
}
