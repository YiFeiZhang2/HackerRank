import java.io.*;
import java.util.*;

public class MaxSubarray {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int numCase = in.nextInt();;
        for(int i = 0; i<numCase; i++){
            int arrLength = in.nextInt();
            int[] arr = new int[arrLength];
            int maxNonContig = 0;
            int maxContig = 0;
            int maxContigHere = 0;
            int arrMax = Integer.MIN_VALUE;
            for(int j = 0; j<arrLength; j++){
                arr[j] = in.nextInt();
                if (arr[j] > arrMax){
                    arrMax = arr[j];
                }
                if (arr[j] > 0) {
                    maxNonContig += arr[j];
                }
                if (maxContigHere + arr[j] > 0){
                    maxContigHere = maxContigHere + arr[j];
                    maxContig = Math.max(maxContigHere, maxContig);
                }
                else{
                    maxContigHere = 0;
                }
            }
            if(arrMax < 0){
                maxContig = arrMax;
                maxNonContig = arrMax;
            }
            System.out.println(maxContig + " " + maxNonContig);
        }
    }
}
