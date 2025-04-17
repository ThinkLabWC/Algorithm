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

public class Main20920 {
	static class Word implements Comparable<Word>{
		String st;
		int len;
		int vindo;

		public Word(String st, int len, int vindo){
			this.st = st;
			this.len = len;
			this.vindo = vindo;
		}

		public int compareTo(Word w){
			if(this.vindo == w.vindo){
				if(this.len == w.len){
					return this.st.compareTo(w.st);
				}
				return w.len - this.len;
			}
			return w.vindo - this.vindo;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] st = br.readLine().split(" ");
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(st[0]);
		int m = Integer.parseInt(st[1]);
		List<Word> words = new ArrayList<>();
		Map<String, Integer> s = new HashMap<>();
		//십만
		for(int i=0; i<n; i++){
			String str = br.readLine();
			if(str.length() >= m){
				s.put(str, s.getOrDefault(str, 1) + 1);
			}
		}
		// System.out.println(s);
		//십만
		List<String> keySet = new ArrayList<>(s.keySet());
		for(int i=0; i<keySet.size(); i++){
			words.add(new Word(keySet.get(i), keySet.get(i).length(), s.get(keySet.get(i))));
		}
		//십만
		Collections.sort(words);
		for(int i=0; i<words.size(); i++){
			sb.append((words.get(i).st + "\n"));
		}
		System.out.println(sb);
	}
}
