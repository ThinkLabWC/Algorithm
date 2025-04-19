package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main1755 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		int a = Integer.parseInt(st[0]);
		int b = Integer.parseInt(st[1]);
		Map<Character, String> s = new HashMap<>();
		s.put('0', "zero");
		s.put('1', "one");
		s.put('2', "two");
		s.put('3', "three");
		s.put('4', "four");
		s.put('5', "five");
		s.put('6', "six");
		s.put('7', "seven");
		s.put('8', "eight");
		s.put('9', "nine");

		Map<String, Character> u = new HashMap<>();
		u.put("zero", '0');
		u.put("one", '1');
		u.put("two", '2');
		u.put("three", '3');
		u.put("four", '4');
		u.put("five", '5');
		u.put("six", '6');
		u.put("seven", '7');
		u.put("eight", '8');
		u.put("nine", '9');

		List<String> lists = new ArrayList<>();
		for(int i=a; i<=b; i++){
			String num = String.valueOf(i);
			String str = "";
			for(int j=0; j<num.length(); j++){
				if(s.containsKey(num.charAt(j))){
					str += s.get(num.charAt(j));
				}
				str += " ";
			}
			// System.out.println("[" + str + "]");
			String trimStr = str.strip();
			// System.out.println("[" + trimStr + "]");
			lists.add(trimStr);
		}
		// System.out.println(lists);
		Collections.sort(lists);
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<lists.size(); i++){
			if(i % 10 == 0 && i != 0){
				sb.append('\n');
			}
			String[] n = lists.get(i).split(" ");
			for(int j=0; j<n.length; j++){
				sb.append(u.get(n[j]));
			}
			sb.append(" ");
		}
		System.out.println(sb);
	}
}
