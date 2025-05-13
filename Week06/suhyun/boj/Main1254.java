package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1254 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int ans = str.length();
		for(int i=0; i<str.length(); i++){
			if(!isPalind(str.substring(i))){
				ans += 1;
			} else {
				break;
			}
		}
		System.out.println(ans);
		// System.out.println(str.substring(1));
	}

	public static boolean isPalind(String s){
		StringBuilder sb = new StringBuilder(s);
		if(s.equals(sb.reverse().toString())){
			return true;
		}
		return false;
	}
}
