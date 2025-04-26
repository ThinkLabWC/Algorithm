package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class Main4889 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int testcase = 0;
		while (true) {
			String str = br.readLine();
			if (str.contains("-")) {
				break;
			}
			char[] c = str.toCharArray();
			testcase += 1;
			sb.append(testcase + ". " + confirm(c) + "\n");
		}
		System.out.println(sb);
	}

	public static int confirm(char[] c) {
		int cnt = 0;
		Stack<Character> stack = new Stack<>();
		for(int i=0; i<c.length; i++){
			if(c[i] == '{'){
				stack.push('{');
			} else {
				if(!stack.isEmpty()){
					stack.pop();
				} else {
					cnt += 1;
					stack.push('{');
				}
			}
		}
		if(!stack.isEmpty()){
			cnt += stack.size() / 2;
		}
		return cnt;
	}
}