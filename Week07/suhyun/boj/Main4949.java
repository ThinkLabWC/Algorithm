package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main4949 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true){
			String str = br.readLine();
			if (str.equals(".")) {
				break;
			}
			Stack<Character> s = new Stack<>(); // [
			boolean balanced = true;
			for(int i=0; i<str.length(); i++){
				if(str.charAt(i) == '['){
					s.add(str.charAt(i));
				}
				if(str.charAt(i) == '('){
					s.add(str.charAt(i));
				}
				if(str.charAt(i) == ']'){
					if(!s.isEmpty() && s.peek() == '['){
						s.pop();
					} else {
						balanced = false;
						break;
					}
				}
				if(str.charAt(i) == ')'){
					if(!s.isEmpty() && s.peek() == '('){
						s.pop();
					} else {
						balanced = false;
						break;
					}
				}
			}
			if(balanced && s.isEmpty()){
				sb.append("yes").append('\n');
			} else {
				sb.append("no").append('\n');
			}
		}
		System.out.println(sb);
	}
}
