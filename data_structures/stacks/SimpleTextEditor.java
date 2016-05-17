import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class SimpleTextEditor {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        Stack<String> text = new Stack<String>();
        StringBuilder sb = new StringBuilder("");
        
        int numInputs = in.nextInt();
        in.nextLine();
        
        for(int i = 1; i<numInputs+1; i++){
            String[] line = in.nextLine().split(" ");
            String type_op = line[0];
            
            if (type_op.equals("1")){
                String input = line[1];
                sb.append(input);
                text.push(sb.toString());
            }
            
            else if (type_op.equals("2")){
                int input = Integer.parseInt(line[1]);
                sb.delete(sb.length()-input, sb.length());
                text.push(sb.toString());
            }
            
            else if (type_op.equals("3")){
                int numChar = Integer.parseInt(line[1]);
                System.out.println(sb.charAt(numChar-1));
            }
            
            else if (type_op.equals("4")){
                if (text.isEmpty()){
                    sb = new StringBuilder("");
                }
                else{
                    text.pop();
                    if(text.isEmpty()){
                        sb = new StringBuilder("");
                    }
                    else{
                        sb = new StringBuilder(text.peek());
                    }
                }
            }
        }
    }
}