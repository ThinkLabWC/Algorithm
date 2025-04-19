package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main2744 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String s = "";
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z'){
				s += String.valueOf(str.charAt(i)).toLowerCase();
			} else {
				s += String.valueOf(str.charAt(i)).toUpperCase();
			}
		}
		System.out.println(s);
	}
}
