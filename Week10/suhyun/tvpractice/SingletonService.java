package Week10.suhyun.tvpractice;

public class SingletonService {
	private static final SingletonService instance = new SingletonService();

	private SingletonService(){

	}

	public static SingletonService getInstance(){
		return instance;
	}
}
