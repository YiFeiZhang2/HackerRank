import java.util.*;
public class IntToString{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		while(in.hasNextInt()){
			int n = in.nextInt();
			String output = String.valueOf(n);
			String output1 = "" + n;
			String output2 = Integer.toString(n);
			System.out.println(output);
			System.out.println(output1);
			System.out.println(output2);
		}
	}
}
