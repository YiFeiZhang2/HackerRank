import java.util.*;
abstract class Book {
	String title;
	String author;
	Book(String t, String a){
		title = t;
		author = a;
	}
	abstract void display();
}

class MyBook extends Book{
	int price;
	
	MyBook(String title, String author, int price){
		super(title, author);
		this.price = price;
	}
	
	void display(){
		System.out.println("Title: " + this.title);
		System.out.println("Author: " + this.author);
		System.out.println("Price: " + this.price);
	}
}

class Solution{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		String title = in.nextLine();
		String author = in.nextLine();
		int price = in.nextInt();
		Book new_novel = new MyBook(title, author, price);
		new_novel.display();
	}
}
