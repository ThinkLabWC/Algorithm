package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main10798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<String> arr = new ArrayList<>();
		String str = "";
		String ans = "";
		while((str = br.readLine()) != null && !str.equals("")){
			arr.add(str);
		}
		// System.out.println(arr);
		int ga = 0;
		for(int i=0; i<arr.size(); i++){
			if(ga < arr.get(i).length()){
				ga = arr.get(i).length();
			}
		}
		// System.out.println(ga);
		for(int j=0; j<ga; j++){
			for(int i=0; i<arr.size(); i++){
				if(arr.get(i).length() <= j){
					continue;
				}
				ans += arr.get(i).charAt(j);
			}
		}
		System.out.println(ans);
	}
}
