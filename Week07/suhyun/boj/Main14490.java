package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main14490 {

	static int val;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(":");
		int a = Integer.parseInt(st[0]);
		int b = Integer.parseInt(st[1]);
		val = 0;
		if(a >= b){
			val = gcd(a, b);
			System.out.println((a / val) + ":" + (b / val));
		} else {
			val = gcd(b, a);
			System.out.println((a / val) + ":" + (b / val));
		}
	}

	public static int gcd(int a, int b){
		if(a % b == 0){
			return b;
		}
		return gcd(b, a % b);
	}
}
