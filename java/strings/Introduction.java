import java.io.*;
import java.util.*;

public class Introduction{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		String A = in.next();
		String B = in.next();
		System.out.println(A.length() + B.length());
		if(A.compareTo(B)>0){
			System.out.println("Yes");
		} else if(A.compareTo(B)<0){
			System.out.println("No");
		} else{
			System.out.println("Equal");
		}
		System.out.println(A.substring(0,1).toUpperCase() + A.substring(1) + " " + B.substring(0,1).toUpperCase() + B.substring(1));
	}
}
