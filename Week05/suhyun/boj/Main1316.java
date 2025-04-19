package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1316 {
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		int ans = 0;
		for(int i=0; i<n; i++){
			int[] alpha = new int[26];
			String s = br.readLine();
			boolean a = false;
			alpha[s.charAt(0) - 'a'] += 1;
			for(int j=1; j<s.length(); j++){
				// System.out.println(s.charAt(j) - 'a');
				alpha[s.charAt(j) - 'a']++;
				if(alpha[s.charAt(j) - 'a'] >= 2){
					if(s.charAt(j) == s.charAt(j-1)){
						continue;
					}
					a = true;
					break;
				}
			}
			if(!a || s.length() == 1){
				ans += 1;
			}
		}
		System.out.println(ans);
	}
}
