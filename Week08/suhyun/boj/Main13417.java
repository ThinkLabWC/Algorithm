package Week08.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main13417 {

	static int t, n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for(int i=0; i<t; i++){
			n = Integer.parseInt(br.readLine());
			// char[] s = br.readLine().toCharArray();
			String[] str = br.readLine().split(" ");
			char[] s = new char[str.length];
			for(int j=0; j<str.length; j++){
				s[j] = str[j].charAt(0);
			}
			// System.out.println(Arrays.toString(s));
			String ans = s[0] + "";
			if(s.length > 1){
				if(ans.charAt(0) >= s[1]){
					ans = String.valueOf(s[1]) + String.valueOf(ans.charAt(0));
				} else {
					ans = String.valueOf(ans.charAt(ans.length() - 1)) + String.valueOf(s[1]);
				}
				// System.out.println(ans);
				for(int j=2; j<s.length; j++){
					//왼쪽 붙이기
					if((ans.charAt(0) >= s[j])){
						ans = String.valueOf(s[j]) + ans;
					} else {
						ans = ans + String.valueOf(s[j]);
					}
					// System.out.println(ans);
				}
			}
			System.out.println(ans);
		}
	}
}
