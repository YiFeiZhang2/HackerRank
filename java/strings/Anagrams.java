import java.io.*;
import java.util.*;

public class Anagrams {
	static boolean isAnagram(String A, String B){
		A = A.toLowerCase();
		B = B.toLowerCase();

		if(A.length()!=B.length()){
			return false;
		} else{
			int[] contained = new int[26];
			for(int i = 0; i<A.length(); i++){
				contained[(int)A.charAt(i)-97] += 1;
				contained[(int)B.charAt(i)-97] -= 1;
			}
			for(int i = 0; i<contained.length; i++){
				if(contained[i]!=0){
					return false;
				}
			}
			return true;
		}
	}
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		String A = in.next();
		String B = in.next();
		if(isAnagram(A,B)){
			System.out.println("Anagram");
		} else{
			System.out.println("Not Anagram");
		}
	}
}
