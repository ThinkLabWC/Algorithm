package Week06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main2204 {

	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true){
			n = Integer.parseInt(br.readLine());
			if(n == 0){
				break;
			}
			List<String> arr = new ArrayList<>();
			Map<String, String> a = new HashMap<>();
			for(int i=0; i<n; i++){
				String str = br.readLine();
				String lower = str.toLowerCase();
				a.put(lower, str);
				arr.add(lower);
			}
			Collections.sort(arr);
			System.out.println(a.get(arr.get(0)));
		}
	}
}
