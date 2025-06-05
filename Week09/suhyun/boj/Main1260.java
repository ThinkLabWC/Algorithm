package Week09.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main1260 {

	static StringTokenizer st;
	static int m, n, v;
	static boolean[] visited;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

	static void dfs(int x){
		visited[x] = true;
		System.out.print(x + " ");
		for(int i=0; i<graph.get(x).size(); i++){
			int y = graph.get(x).get(i);
			if(!visited[y]){
				dfs(y);
			}
		}
	}

	static void bfs(int x){
		Queue<Integer> q = new LinkedList<>();
		visited[x] = true;
		q.offer(x);
		while(!q.isEmpty()){
			int y = q.poll();
			System.out.print(y + " ");
			for(int i=0; i<graph.get(y).size(); i++){
				int a = graph.get(y).get(i);
				if(!visited[a]){
					visited[a] = true;
					q.offer(a);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		v = Integer.parseInt(st.nextToken());
		visited = new boolean[n + 1];

		for(int i=0; i<n+1; i++){
			graph.add(new ArrayList<Integer>());
		}

		for(int i=0; i<m; i++){
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		for(int i=1; i<=n; i++){
			Collections.sort(graph.get(i));
		}

		dfs(v);
		visited = new boolean[n + 1];
		System.out.println();
		bfs(v);
	}
}
