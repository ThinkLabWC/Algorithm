package Week10.suhyun.tvpractice;

public interface Singer {
	void sing(String s);
	private static void nabi(String s){
		System.out.println("수현");
	};
	default void a(){
		nabi("수현");
		System.out.println("A");
	};
	static void b(){
		nabi("수현");
		System.out.println("B");
	}
}
