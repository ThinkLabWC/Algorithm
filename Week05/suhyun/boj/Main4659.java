package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main4659 {

	static Set<Character> mo = new HashSet<>();

	public static void main(String[] args) throws IOException {
		mo.add('a');
		mo.add('e');
		mo.add('i');
		mo.add('o');
		mo.add('u');
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true){
			String st = br.readLine();
			if(st.equals("end")){
				break;
			}
			if(containMoum(st) && (!mo_three(st) && !za_three(st)) && !sa(st)){
				sb.append("<");
				sb.append(st + ">");
				sb.append(" is acceptable.\n");
			} else {
				sb.append("<");
				sb.append(st + ">");
				sb.append(" is not acceptable.\n");
			}
		}
		System.out.println(sb);
	}

	public static boolean sa(String str){
		char z = str.charAt(0);
		char e = 'e';
		char o = 'o';
		for(int i=1; i<str.length(); i++){
			if(z == str.charAt(i)){
				if(z == 'e' || z == 'o'){
					continue;
				}
				return true;
			} else {
				z = str.charAt(i);
			}
		}
		return false;
	}

	public static boolean mo_three(String str){
		int mo_cnt = 0;
		for(int i=0; i<str.length(); i++){
			if(mo.contains(str.charAt(i))){
				mo_cnt += 1;
			} else {
				mo_cnt = 0;
			}

			if(mo_cnt >= 3){
				return true;
			}
		}
		return false;
	}

	public static boolean za_three(String str){
		int za_cnt = 0;
		for(int i=0; i<str.length(); i++){
			if(!mo.contains(str.charAt(i))){
				za_cnt += 1;
			} else {
				za_cnt = 0;
			}

			if(za_cnt >= 3){
				return true;
			}
		}
		return false;
	}

	public static boolean containMoum(String str){
		for(int i=0; i<str.length(); i++){
			if(mo.contains(str.charAt(i))){
				return true;
			}
		}
		return false;
	}
}
