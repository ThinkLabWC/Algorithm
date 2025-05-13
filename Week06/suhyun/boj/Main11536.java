package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main11536 {
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		List<String> arr1= new ArrayList<>();
		List<String> arr2 = new ArrayList<>(); // 오름
		List<String> arr3 = new ArrayList<>(); // 내림
		for(int i=0; i<n; i++){
			String name = br.readLine();
			arr1.add(name);
			arr2.add(name);
			arr3.add(name);
		}
		Collections.sort(arr2);
		Collections.sort(arr3, Collections.reverseOrder());
		int ans = 0; // -1, 0, 1(증가, 감소, 이것도 저것도 아님)
		for(int i=0; i<arr1.size(); i++){
			if(arr1.get(i) == arr2.get(i)){
				ans = -1;
			} else if(arr1.get(i) == arr3.get(i)){
				ans = 0;
			} else {
				ans = 1;
				break;
			}
		}
		if(ans == -1){
			System.out.println("INCREASING");
		} else if(ans == 0){
			System.out.println("DECREASING");
		} else {
			System.out.println("NEITHER");
		}
	}
}
