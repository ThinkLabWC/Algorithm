package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

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
