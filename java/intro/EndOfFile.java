import java.io.*;
import java.util.*;

public class EndOfFile {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int counter = 1;
        while(in.hasNextLine()){
            System.out.println(counter + " " + in.nextLine());
            counter ++;
        }
    }
}
