package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main11656 {

	static List<String> arr = new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		for(int i=0; i<str.length(); i++){
			arr.add(str.substring(i));
		}
		Collections.sort(arr);
		for(int i=0; i<arr.size(); i++){
			System.out.println(arr.get(i));
		}
	}
}
