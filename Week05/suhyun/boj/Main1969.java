package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main1969 {
	static int n,m;
	static Map<Character, Integer> dna = new HashMap<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		n = Integer.parseInt(str[0]);
		m = Integer.parseInt(str[1]);
		List<String> words = new ArrayList<>();
		// A - 0, C - 1, G - 2, T - 3
		char[] dna = new char[m];
		// 결국 dna를 출력하도록 // 가장 많이 등장한 알파벳을 넣기
		for(int i=0; i<n; i++){
			String st = br.readLine();
			words.add(st);
		}
		int[][] vindo = new int[m][4];
		for(int j=0; j<m; j++){
			for(int i=0; i<n; i++){
				char c = words.get(i).charAt(j);
				if(c == 'A'){
					vindo[j][0] += 1;
				} else if(c == 'C'){
					vindo[j][1] += 1;
				} else if(c == 'G'){
					vindo[j][2] += 1;
				} else {
					vindo[j][3] += 1;
				}
			}
		}
		// for(int i=0; i<m; i++){
		// 	for(int k=0; k<4; k++){
		// 		System.out.print(vindo[i][k] + " ");
		// 	}
		// 	System.out.println();
		// }
		// int ans = 0;
		for(int i=0; i<m; i++){
			int max = 0;
			char alpha = ' ';
			for(int j=0; j<4; j++){
				if(vindo[i][j] > max){
					max = vindo[i][j];
					if(j == 0){
						alpha = 'A';
					} else if(j == 1){
						alpha = 'C';
					} else if(j == 2){
						alpha = 'G';
					} else {
						alpha = 'T';
					}
				};
			}
			// if(!same){
			// 	ans += 1;
			// }
			dna[i] = alpha;
		}
		int ans = 0;
		for(int i=0; i<words.size(); i++){
			for(int j=0; j<m; j++){
				if(words.get(i).charAt(j) != dna[j]){
					ans += 1;
				}
			}
		}
		for(int i=0; i<m; i++){
			System.out.print(dna[i]);
		}
		System.out.println();
		System.out.println(ans);
	}
}
