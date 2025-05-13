package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main2941 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		char[] cro = str.toCharArray();
		// System.out.println(Arrays.toString(cro));
		int ans = 0;
		int idx = 0;
		Set<String> a = new HashSet<>();
		a.add("c=");
		a.add("c-");
		a.add("dz=");
		a.add("d-");
		a.add("lj");
		a.add("nj");
		a.add("s=");
		a.add("z=");
		while(idx < cro.length){
			if(idx < cro.length - 1){
				if(a.contains(String.valueOf(cro[idx]) + String.valueOf(cro[idx + 1]))){
					idx += 2;
					ans += 1;
					continue;
				}
			}
			if(idx < cro.length - 2){
				if(a.contains(String.valueOf(cro[idx]) + String.valueOf(cro[idx + 1]) + String.valueOf(cro[idx + 2]))){
					idx += 3;
					ans += 1;
					continue;
				}
			}
			ans += 1;
			idx += 1;
		}
		System.out.println(ans);
	}
}
