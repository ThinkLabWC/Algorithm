package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1543 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		String b = br.readLine();
		int cnt = 0;
		while(true){
			if(a.contains(b)){
				int idx = a.indexOf(b);
				if(idx == -1){
					break;
				}
				a = a.substring(idx + b.length());
				cnt += 1;
				// System.out.println(a);
			} else {
				break;
			}
		}
		System.out.println(cnt);
	}
}
