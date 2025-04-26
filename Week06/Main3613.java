package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.regex.Pattern;

public class Main3613 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		if(isJava(str)){
			System.out.println(javaToC(str));
		} else if(isC(str)){
			System.out.println(cToJava(str));
		} else {
			System.out.println("Error!");
		}
	}

	public static String cToJava(String str){
		return Pattern.compile("_(.)")
			.matcher(str)
			.replaceAll(m -> m.group(1).toUpperCase());
	}

	// 자바 -> C
	public static String javaToC(String str){
		StringBuilder sb = new StringBuilder(str);
		for(int i=0; i<sb.length(); i++){
			char ch = sb.charAt(i);
			if(ch >= 'A' && ch <= 'Z'){
				sb.replace(i, i+1, String.valueOf(ch).toLowerCase());
				sb.insert(i, "_");
			}
		}
		return sb.toString();
	}

	public static boolean isC(String str){
		if(str.charAt(str.length() - 1) == '_'){
			return false;
		} else if(str.charAt(0) == '_'){
			return false;
		} else if(str.contains("__")){
			return false;
		}
		else {
			boolean confirm = true;
			String[] parts = str.split("_");
			for(int i=0; i<parts.length; i++){
				for(int j=0; j<parts[i].length(); j++){
					if(!Character.isLowerCase(parts[i].charAt(j))){
						confirm = false;
						break;
					}
				}
			}
			return confirm;
		}
	}

	public static boolean isJava(String str){
		String[] parts = str.split("(?=[A-Z])");
		boolean confirm = true;
		for(int i=0; i<parts.length; i++){
			char[] word = parts[i].toCharArray();
			if(i == 0){
				for(int j=0; j<word.length; j++){
					if(!Character.isLowerCase(word[j])){
						confirm = false;
						break;
					}
				}
			} else {
				for(int j=0; j<word.length; j++){
					if(j == 0){
						if(!Character.isUpperCase(word[j])){
							confirm = false;
						}
					} else {
						if(!Character.isLowerCase(word[j])){
							confirm = false;
						}
					}
				}
			}
		}
		return confirm;
	}
}
