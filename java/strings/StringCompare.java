import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class StringCompare {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        int length = in.nextInt();
        String minSub = line.substring(0,length);
        String maxSub = line.substring(0,length);
        for(int i = 0; i<=line.length()-length; i++){
            String subString = line.substring(i,i+length);
            if (subString.compareTo(minSub)<0){
                minSub = subString;
            }
            if (subString.compareTo(maxSub)>0){
                maxSub = subString;
            }
        }
        System.out.println(minSub);
        System.out.println(maxSub);
    }
}
