package Week08.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main14425 {
	static int n,m, ans;
	static List<String> list = new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		n = Integer.parseInt(s[0]);
		m = Integer.parseInt(s[1]);
		for(int i=0; i<n; i++){
			list.add(br.readLine());
		}
		ans = 0;
		for(int i=0; i<m; i++){
			String target = br.readLine();
			for(int j=0; j<n; j++){
				if(list.get(j).equals(target)){
					ans += 1;
					// System.out.println(target);
				}
			}
		}
		System.out.println(ans);
	}
}
