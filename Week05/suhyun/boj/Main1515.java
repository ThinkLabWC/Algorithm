package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 234092
// 20
public class Main1515 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int idx = 0;
		int num = 1;
		//10과
		while(idx < s.length()){
			String sn = String.valueOf(num);// 10
			for(int i=0; i<sn.length(); i++){
				if(idx < s.length() && s.charAt(idx) == sn.charAt(i)){
					idx++;
				}
			}
			num++;
		}
		System.out.println(num - 1);
	}
}
