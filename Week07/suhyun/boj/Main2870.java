package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main2870 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		List<String> arr = new ArrayList<>();
		for(int i=0; i<n; i++){
			String str = br.readLine();
			String a = "";
			for(int j=0; j<str.length(); j++){
				if(str.charAt(j) >= '0' && str.charAt(j) <= '9'){
					if(j == 0 && str.charAt(j) == '0'){
						continue;
					}
					a += str.charAt(j) + "";
				} else {
					if (!a.equals("")) {
						arr.add(a);
					}
					a = "";
				}
			}
			if (!a.equals("")) {
				arr.add(a);
			}
			// System.out.println(arr);
		}
		// System.out.println(arr);
		List<String> ans = new ArrayList<>();
		for(int i=0; i<arr.size(); i++){
			if(isNumberic(arr.get(i))){
				if(isAllZero(arr.get(i))){
					ans.add("0");
				} else {
					ans.add(stringToNumber(arr.get(i)));
				}
			}
		}
		Collections.sort(ans, (a, b) -> new BigInteger(a).compareTo(new BigInteger(b)));
		// System.out.println(ans);
		for(int i=0; i<ans.size(); i++){
			sb.append(ans.get(i)).append('\n');
		}
		System.out.println(sb);
	}

	public static boolean isNumberic(String str){
		return str.chars().allMatch(Character::isDigit);
	}

	public static boolean isAllZero(String str){
		return str.chars().allMatch(c -> c == '0');
	}

	public static String stringToNumber(String str){
		boolean zero = false;
		int zero_idx = 0;
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) != '0'){
				zero = false;
				zero_idx = i;
				break;
			}
		}
		return str.substring(zero_idx);
	}
}
