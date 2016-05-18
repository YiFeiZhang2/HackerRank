import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JavaStringReverse {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
	Method2(line);
    }
    public static void Method2(String line){
	System.out.println(line.equals(new StringBuilder(line).reverse().toString()) ? "Yes" : "No" );
    }
}
