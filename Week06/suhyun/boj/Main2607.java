package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main2607 {

	static int n;
	static String str;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		List<String> a = new ArrayList<>();
		str = br.readLine();
		for(int i=0; i<n-1; i++){
			a.add(br.readLine());
		}
		int ans = 0;
		for(int i=0; i<a.size(); i++){
			int cnt = 0;
			for(int j=0; j<str.length(); j++){
				if(a.get(i).contains(str.charAt(j) + "")){
					cnt += 1;
				}
			}
			if(cnt == 3){
				if(a.get(i).length() - 1 == str.length() || a.get(i).length() == str.length()){
					ans += 1;
				}
			} else if(cnt == 2 && str.length() == a.get(i).length()){
				ans += 1;
			} else if(cnt == 2 && str.length() == a.get(i).length() + 1){
				ans += 1;
			}
		}
		System.out.println(ans);
	}
}
