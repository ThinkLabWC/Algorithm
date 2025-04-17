package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1157 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String st = br.readLine().toUpperCase();
		char[] alpha = new char[26];
		for(int i=0; i<st.length(); i++){
			alpha[st.charAt(i) - 'A'] += 1;
		}
		int max = 0;
		char ans = ' ';
		for(int i=0; i<alpha.length; i++){
			if(max < alpha[i]){
				ans = (char)(i + 'A');
				max = alpha[i];
			} else if(max == alpha[i]){
				ans = '?';
			}
		}
		System.out.println(ans);
	}
}
