package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main4659 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true){
			String str = br.readLine();
			if(str.equals("end")){
				break;
			}
			if(containMoum(str) && !confirm3M(str) && !confrim3J(str) && !confrim2(str)){
				sb.append("<" + str + "> is acceptable.\n");
			} else {
				sb.append("<" + str + "> is not acceptable.\n");
			}
		}
		System.out.println(sb);
	}

	static boolean containMoum(String str){
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
				return true;
			}
		}
		return false;
	}

	static boolean confirm3M(String str){
		int mo = 0;
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
				mo += 1;
			} else {
				mo = 0;
			}
			if(mo >= 3){
				return true;
			}
		}
		return false;
	}

	static boolean confrim3J(String str){
		int za = 0;
		for(int i=0; i<str.length(); i++){
			if(str.charAt(i) != 'a' && str.charAt(i) != 'e' && str.charAt(i) != 'i' && str.charAt(i) != 'o' && str.charAt(i) != 'u'){
				za += 1;
			} else {
				za = 0;
			}
			if(za >= 3){
				return true;
			}
		}
		return false;
	}

	static boolean confrim2(String str){
		for(int i=0; i<str.length()-1; i++){
			if(str.charAt(i) == str.charAt(i + 1)){
				if(str.charAt(i) != 'e' && str.charAt(i) != 'o'){
					return true;
				}
			}
		}
		return false;
	}
}
