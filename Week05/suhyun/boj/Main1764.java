package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main1764 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int n = Integer.parseInt(st[0]);
		int m = Integer.parseInt(st[1]);
		int ans = 0;
		// StringBuilder sb = new StringBuilder();
		List<String> s = new ArrayList<>();
		Set<String> hear = new HashSet<>();
		for(int i=0; i<n; i++){
			hear.add(br.readLine());
		}
		// System.out.println(hear);
		for(int i=0; i<m; i++){
			String str = br.readLine();
			if(hear.contains(str)){
				ans += 1;
				s.add(str);
			}
		}
		Collections.sort(s);
		System.out.println(ans);
		for(int i=0; i<s.size(); i++){
			System.out.println(s.get(i));
		}
	}
}
