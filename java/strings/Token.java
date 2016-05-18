import java.io.*;
import java.util.*;

public class Token{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		String line = in.nextLine();
		if(line.length()>400000||line.trim().length()==0){
			System.out.println("0");
		} else{
			String[] output = line.trim().split("[ !,?._'@\\ ]+");
			System.out.println(output.length);
			for(String word:output){
				System.out.println(word);
			}
		}
	}
}
