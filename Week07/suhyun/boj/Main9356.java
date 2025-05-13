package Week07.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main9356 {

	static int t;
	static List<String> fox;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for(int i=0; i<t; i++){
			while(true){
				String str = br.readLine();
				if(str.equals("what does the fox say?")){
					break;
				}
				if(str.contains("goes")){
					String[] not_fox = str.split(" ");
					for(int j=0; j<fox.size(); j++){
						if(fox.get(j).contains(not_fox[2])){
							fox.removeAll(Arrays.asList(not_fox[2]));
						}
					}
				} else {
					fox = new ArrayList<>(Arrays.asList(str.split(" ")));
				}
			}
			// System.out.println(fox);
			for(int j=0; j<fox.size(); j++){
				sb.append(fox.get(j) + " ");
			}
			sb.append('\n');
		}
		System.out.println(sb);
	}
}
