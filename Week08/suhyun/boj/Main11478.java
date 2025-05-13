package Week08.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main11478 {

	static Set<String> z;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		z = new HashSet<>();
		pro(s);
		System.out.println(z.size());
	}

	static void pro(String s){
		for(int L=0; L<s.length(); L++){
			String str = "";
			int R = L;
			while(R < s.length()){
				str += s.charAt(R++);
				z.add(str);
				// System.out.println(str);
			}
		}
	}
}
