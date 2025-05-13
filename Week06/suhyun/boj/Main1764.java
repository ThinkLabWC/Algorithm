package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main1764 {

	static int n, m;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int n = Integer.parseInt(st[0]);
		int m = Integer.parseInt(st[1]);
		int cnt = 0;
		StringBuilder sb = new StringBuilder();
		Set<String> hear = new HashSet<>();
		List<String> ans = new ArrayList<>();
		for(int i=0; i<n; i++){
			hear.add(br.readLine());
		}
		for(int i=0; i<m; i++){
			String name = br.readLine();
			if(hear.contains(name)){
				cnt += 1;
				ans.add(name);
			}
		}
		System.out.println(cnt);
		Collections.sort(ans);
		for(int i=0; i<ans.size(); i++){
			System.out.println(ans.get(i));
		}
	}
}
