package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main1302 {

	static class Book implements Comparable<Book>{
		String name;
		int cnt;

		public Book(String name, int cnt){
			this.name = name;
			this.cnt = cnt;
		}

		public int compareTo(Book b){
			if(b.cnt == this.cnt){
				return this.name.compareTo(b.name);
			}
			return b.cnt - this.cnt;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		Map<String, Integer> books = new HashMap<>();
		List<Book> seller = new ArrayList<>();
		for(int i=0; i<n; i++){
			String b = br.readLine();
			books.put(b, books.getOrDefault(b, 1) + 1);
		}
		List<String> bs = new ArrayList<>(books.keySet());
		for(int i=0; i<bs.size(); i++){
			seller.add(new Book(bs.get(i), books.get(bs.get(i))));
		}
		Collections.sort(seller);
		// int max = seller.get(0).cnt;
		// for(int i=0; i<seller.size(); i++){
		// 	if(max == seller.get(i).cnt){
		// 		sb.append(seller.get(i).name + "\n");
		// 	} else {
		// 		break;
		// 	}
		// }
		System.out.println(seller.get(0).name);
	}
}
