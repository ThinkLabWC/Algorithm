package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main1620 {

	static int n, m;
	static Map<String, Integer> s = new HashMap<>();
	static Map<Integer, String> u = new HashMap<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		n = Integer.parseInt(st[0]);
		m = Integer.parseInt(st[1]);
		for(int i=1; i<=n; i++){
			String str = br.readLine();
			s.put(str, i);
			u.put(i, str);
		}
		// System.out.println(s);
		// System.out.println(u);
		for(int i=0; i<m; i++){
			String str = br.readLine();
			if(str.charAt(0) >= '1' && str.charAt(0) <= '9'){
				int num = Integer.parseInt(str);
				// System.out.println(num);
				System.out.println(u.get(num));
			} else {
				System.out.println(s.get(str));
			}
		}
	}
}
