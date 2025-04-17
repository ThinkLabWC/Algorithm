package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main7785 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Set<String> s = new HashSet<>();
		for(int i=0; i<n; i++){
			String[] ss = br.readLine().split(" ");
			if(ss[1].equals("enter")){
				s.add(ss[0]);
			} else {
				s.remove(ss[0]);
			}
		}
		List<String> k = new ArrayList<>(s);
		Collections.sort(k, Collections.reverseOrder());
		for(int i=0; i<k.size(); i++){
			System.out.println(k.get(i));
		}
	}
}
