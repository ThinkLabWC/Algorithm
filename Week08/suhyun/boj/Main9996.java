package Week08.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main9996 {

	static int n;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		String file = br.readLine();
		int file_len = file.length();
		for(int i=0; i<n; i++){
			String n = br.readLine();
			boolean same = true;
			int n_len = n.length();
			String[] f = file.split("\\*");
			String star = "";
			for(int k=0; k<n_len-(f[0].length() + f[1].length()); k++){
				star += "*";
			}
			String s = f[0] + star + f[1];
			// System.out.println(s);
			if(s.length() > n.length()){
				same = false;
			} else {
				for(int k=0; k<s.length(); k++){
					if(s.charAt(k) != '*' && s.charAt(k) != n.charAt(k)){
						same = false;
					}
				}
			}
			if(same){
				sb.append("DA").append('\n');
			} else {
				sb.append("NE").append('\n');
			}
		}
		System.out.println(sb);
	}
}
