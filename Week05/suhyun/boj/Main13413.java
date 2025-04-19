package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main13413 {

	static int t, n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for(int i=0; i<t; i++){
			n = Integer.parseInt(br.readLine());
			String str1 = br.readLine();
			String str2 = br.readLine();

			int blackToWhite = 0;
			int whiteToBlack = 0;
			for(int j=0; j<n; j++){
				if(str1.charAt(j) != str2.charAt(j)){
					if(str1.charAt(j) == 'B'){
						blackToWhite++;
					} else {
						whiteToBlack++;
					}
				}
			}

			int ans = Math.max(blackToWhite, whiteToBlack);
			System.out.println(ans);
		}
	}
}
