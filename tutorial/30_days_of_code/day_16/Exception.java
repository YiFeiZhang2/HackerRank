import java.util.Scanner;

class Exception{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		try{
			System.out.println(Integer.parseInt(in.nextLine()));
		}
		catch (NumberFormatException nfe) {
			System.out.println("Bad String");
		}
	}
}
