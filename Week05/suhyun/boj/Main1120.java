package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1120 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		if(str[0].length() == str[1].length()){
			int a = 0;
			for(int i=0; i<str[0].length(); i++){
				if(str[0].charAt(i) != str[1].charAt(i)){
					a += 1;
				}
			}
			System.out.println(a);
		} else {
			int front = str[0].length();
			int next = str[1].length();
			int ans = next;
			for(int j=0; j<=next-front; j++){
				int idx = 0;
				int m = 0;
				for(int i=j; i<front+j; i++){
					// if(front <= i){
					// 	continue;
					// }
					if(str[0].charAt(idx) != str[1].charAt(i)){
						m += 1;
					}
					idx += 1;
				}
				// System.out.println(ans + " " + m);
				ans = Math.min(ans, m);
				// System.out.println(ans);
			}
			System.out.println(ans);
		}
	}
}
