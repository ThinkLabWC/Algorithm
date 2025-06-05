package Week09.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main2667 {

	static int n;
	static int[][] graph;
	static String st;
	static boolean[][] visited;
	static int[][] d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
	static ArrayList<Integer> house = new ArrayList<>();
	static int sum;

	static void dfs(int x, int y){
		visited[x][y] = true;
		sum += 1;

		for(int i=0; i<d.length; i++){
			int xx = x + d[i][0];
			int yy = y + d[i][1];

			if(xx < 0 || yy < 0 || xx >= n || yy >= n || visited[xx][yy]){
				continue;
			}

			if(!visited[xx][yy] && graph[xx][yy] == 1){
				dfs(xx, yy);
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		graph = new int[n][n];
		visited = new boolean[n][n];
		for(int i=0; i<n; i++){
			st = br.readLine();
			for(int j=0; j<n; j++){
				graph[i][j] = Integer.parseInt(st.charAt(j) + "");
			}
		}

		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(graph[i][j] == 1 && !visited[i][j]){
					dfs(i, j);
					house.add(sum);
					sum = 0;
				}
			}
		}

		Collections.sort(house);
		System.out.println(house.size());
		for(int i=0; i<house.size(); i++){
			System.out.println(house.get(i));
		}
	}
}
