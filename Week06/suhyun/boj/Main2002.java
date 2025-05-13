package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

public class Main2002 {
	static int n;
	static Map<String, Integer> incars = new LinkedHashMap<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++){
			incars.put(br.readLine(), i);
		}
		int ans = 0;
		for(int i=0; i<n; i++){
			String outcar = br.readLine();
			Iterator<String> it = incars.keySet().iterator();
			while(it.hasNext()){
				if(incars.get(outcar) > incars.get(it.next())){
					ans += 1;
					break;
				}
			}
			incars.remove(outcar);
		}
		System.out.println(ans);
	}
}
