package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main5568 {

	public static Set<String> card = new HashSet<>();
	public static boolean[] visited;
	public static int[] cards;
	public static int n, k;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		k = Integer.parseInt(br.readLine());
		cards = new int[n];
		visited = new boolean[n];
		for(int i=0; i<cards.length; i++){
			cards[i] = Integer.parseInt(br.readLine());
		}
		bfs("", 0);
		// System.out.println(card);
		System.out.println(card.size());
	}

	public static void bfs(String s, int level){
		if(level == k){
			card.add(s);
			// System.out.println("num = " + s);
			return;
		}
		Set<Integer> card = new HashSet<>();
		for(int i=0; i<cards.length; i++){
			if(!visited[i]){
				visited[i] = true;
				// s += String.valueOf(cards[i]);
				bfs(s + String.valueOf(cards[i]), level + 1);
				// bfs(s, level + 1);
				visited[i] = false;
			}
		}
	}
}
