package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main12871 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		String t = br.readLine();
		String a = s + t;
		String b = t + s;
		if(a.equals(b)){
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}
