package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main11899 {

	static String str;
	static int cnt;
	static Stack<Character> stack = new Stack<>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		str = br.readLine();
		cnt = 0;
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) == '('){
				stack.push(str.charAt(i));
			} else {
				if(stack.isEmpty()){
					cnt += 1;
				} else {
					if(stack.peek() == '('){
						stack.pop();
					} else {
						cnt += 1;
					}
				}
			};
		}

		while(!stack.isEmpty()){
			stack.pop();
			cnt += 1;
		}

		System.out.println(cnt);
	}
}
