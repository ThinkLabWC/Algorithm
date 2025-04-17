package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

//getOrDefault, containsKey, get, put
// 맵.forEach((key, value) -> { });
// Iterator<Character> keys = 맵.keySet().iterator();
public class Main9046 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		// char[] alpha = new char[26];
		for(int i=0; i<n; i++){
			char ans = '?';
			Map<Character, Integer> alpha = new HashMap<Character, Integer>();
			for(char a = 'a'; a<='z'; a++){
				alpha.put(a, alpha.getOrDefault(a, 0));
				// System.out.println(a);
			}
			// alpha.forEach((key, value) -> {
			// 	System.out.println(key + " : " + value);
			// });
			String st = br.readLine();
			for(int j=0; j<st.length(); j++){
				char c = st.charAt(j);
				if(alpha.containsKey(c)){
					alpha.put(c, alpha.get(c) + 1);
				}
			}
			// System.out.println(alpha);
			// Collection<Integer> vindo = alpha.values();
			// List<Integer> arr = new ArrayList<>(vindo);
			// Collections.sort(arr, Collections.reverseOrder());
			//1/  최대값 가져오기
			int max = 0;
			int count = 0;
			Iterator<Character> keys = alpha.keySet().iterator();
			while(keys.hasNext()){
				Character k = keys.next();
				if(max < alpha.get(k)){
					max = alpha.get(k);
					ans = k;
				};
			}

			// 2. 최대값 기준으로 문자가 몇개 있는지?
			keys = alpha.keySet().iterator();
			while(keys.hasNext()){
				Character k = keys.next();
				if(max == alpha.get(k)){
					count += 1;
				};
			}

			System.out.println(count == 1 ? ans : "?");
		}
	}
}
