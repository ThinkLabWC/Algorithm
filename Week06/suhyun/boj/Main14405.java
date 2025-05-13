package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main14405 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] s = str.split("pi|ka|chu");
		// System.out.println(Arrays.toString(s));
		if(s.length == 0){
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}
}
