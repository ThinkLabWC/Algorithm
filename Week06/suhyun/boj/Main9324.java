package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main9324 {

	static int n;
	static String str;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++){
			boolean confirm = false;
			int[] alpha = new int[26];
			str = br.readLine();
			for(int j=0; j<str.length(); j++){
				alpha[str.charAt(j) - 'A'] += 1;
				if(alpha[str.charAt(j) - 'A'] == 3){
					if(j == str.length() - 1){
						confirm = true;
						break;
					}
					if(str.charAt(j) != str.charAt(j + 1)){
						confirm = true;
						break;
					} else {
						alpha[str.charAt(j) - 'A'] = 0;
						j++;
					}
				}
			}
			if(confirm){
				System.out.println("FAKE");
			} else {
				System.out.println("OK");
			}
		}
	}
}
