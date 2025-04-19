package Week05.suhyun.boj;

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

//12:32
public class Main4358 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Map<String, Integer> trees = new HashMap<>();
		StringBuilder sb = new StringBuilder();
		double cnt = 0.0;
		//백만
		while(true){
			String str = br.readLine();
			if(str == null || str.equals("")){
				break;
			}
			cnt += 1;
			trees.put(str, trees.getOrDefault(str, 0) + 1);
		}
		// System.out.println(trees);
		// System.out.println(cnt);
		List<String> ans = new ArrayList<>();
		//백만
		for(Map.Entry<String, Integer> entry : trees.entrySet()){
			ans.add(entry.getKey());
		}
		//백만log백만
		Collections.sort(ans);
		for(int i=0; i<ans.size(); i++){
			double ratio = ((trees.get(ans.get(i))) / (cnt)) * 100;
			// System.out.println(ratio);
			// double ration = (Math.round(ratio * 10000)/ 10000.0);
			sb.append(ans.get(i) + " " + String.format("%.4f", ratio) + "\n");
			// sb.append('\n');
		}
		System.out.println(sb);
	}
}
