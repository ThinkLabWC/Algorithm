package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1172002 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		int sum = 0;
		for(int i=0; i<n; i++){
			int num = str.charAt(i) - '0';
			sum += num;
		}
		System.out.println(sum);
	}
}
