package Week08.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main200302 {

	static int n, m;
	static String[] s;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		s = br.readLine().split(" ");
		n = Integer.parseInt(s[0]);
		m = Integer.parseInt(s[1]);
		s = br.readLine().split(" ");
		arr = new int[s.length];
		for(int i=0; i<arr.length; i++){
			arr[i] = Integer.parseInt(s[i]);
		}
		pro();
	}

	static void pro(){
		int R = 0, count = 0, sum = 0;
		for(int L=0; L<arr.length; L++){
			while(arr.length > R && sum < m){
				sum += arr[R++];
			}

			if(sum >= m){
				if(sum == m){
					count += 1;
				}
				sum -= arr[L];
			}
		}
		System.out.println(count);
	}
}
