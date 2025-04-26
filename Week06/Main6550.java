package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main6550 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true){
			String st = br.readLine();
			if(st == null || st.isEmpty()){
				break;
			}
			String[] str = st.split(" ");
			if(confirm(str[0], str[1])){
				sb.append("Yes").append('\n');
			} else {
				sb.append("No").append('\n');
			}
		}
		System.out.println(sb);
	}

	public static boolean confirm(String s, String t){
		Queue<Character> q = new LinkedList<>();
		for(int i=0; i<s.length(); i++){
			q.offer(s.charAt(i));
		}
		for(int i=0; i<t.length(); i++){
			if (!q.isEmpty()) {
				if(q.peek() == t.charAt(i)){
					q.poll();
				}
			}
		}
		return q.isEmpty();
	}
}
