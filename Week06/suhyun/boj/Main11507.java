package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main11507 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] p = new int[14];
		int[] k = new int[14];
		int[] s = new int[14];
		int[] t = new int[14];
		String str = br.readLine();
		for(int i=0; i<str.length()-2; i+=3){
			if(str.charAt(i) == 'P'){
				int num = Integer.parseInt(str.substring(i+1, i+3));
				p[num] += 1;
			} else if(str.charAt(i) == 'K'){
				int num = Integer.parseInt(str.substring(i+1, i+3));
				k[num] += 1;
			} else if(str.charAt(i) == 'H'){
				int num = Integer.parseInt(str.substring(i+1, i+3));
				s[num] += 1;
			} else if(str.charAt(i) == 'T'){
				int num = Integer.parseInt(str.substring(i+1, i+3));
				t[num] += 1;
			}
		}
		// System.out.println(Arrays.toString(p));
		// System.out.println(Arrays.toString(k));
		// System.out.println(Arrays.toString(s));
		// System.out.println(Arrays.toString(t));
		boolean same = false;
		for(int i=1; i<14; i++){
			if(p[i] > 1 || k[i] > 1 || s[i] > 1 || t[i] > 1){
				same = true;
				System.out.println("GRESKA");
			}
		}
		int p_sum = 0;
		int k_sum = 0;
		int s_sum = 0;
		int t_sum = 0;
		if(!same){
			for(int i=1; i<14; i++){
				p_sum += p[i];
				k_sum += k[i];
				s_sum += s[i];
				t_sum += t[i];
			}
			System.out.println((13 - p_sum) + " " + (13 - k_sum) + " " + (13 - s_sum) + " " + (13 - t_sum));
		}
	}
}
