package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main2992 {

	static Set<String> lists = new HashSet<>();
	static String str;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		str = br.readLine();
		visited = new boolean[str.length()];
		dfs("", 0);
		// System.out.println(lists);
		List<String> ans = new ArrayList<>(lists);
		Collections.sort(ans);
		int idx = 0;
		for(int i=0; i<ans.size(); i++){
			if(ans.get(i).equals(str)){
				idx = i + 1;
				break;
			}
		}
		// System.out.println(ans);
		// System.out.println(idx);
		if(idx >= ans.size()){
			System.out.println("0");
		} else {
			System.out.println(ans.get(idx));
		}
	}

	public static void dfs(String s, int depth){
		if(str.length() == depth){
			// System.out.println(s);
			lists.add(s);
			return;
		}

		for(int i=0; i<str.length(); i++){
			if(!visited[i]){
				visited[i] = true;
				dfs(s + str.charAt(i), depth + 1);
				visited[i] = false;
			}
		}
	}
}
