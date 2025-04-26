package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main10610 {

	static String str;
	static boolean[] visited;
	static String max;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		str = br.readLine();
		if(!str.contains("0")){
			System.out.println(-1);
		} else {
			max = "";
			visited = new boolean[str.length()];
			brute_force("");
			System.out.println();
		}
	}

	static void brute_force(String st){
		if(st.length() == str.length()){
			int val = Integer.parseInt(st);
			if(val % 30 == 0){
				// max = Math.max(Integer.parseInt(st), max);
				// Arrays.sort(st, )
			}
			return;
		}

		for(int i=0; i<str.length(); i++){
			if(!visited[i]){
				visited[i] = true;
				brute_force(st + str.charAt(i));
				visited[i] = false;
			}
		}
	}
}
