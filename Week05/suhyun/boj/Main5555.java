package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main5555 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String target = br.readLine();
		String t;
		int cnt = 0;
		int n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++){
			t = br.readLine();
			t += t;

			if(t.contains(target)){
				cnt++;
			}
		}
		System.out.println(cnt);
	}
}
