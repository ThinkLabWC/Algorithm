package Week10.suhyun.tvpractice;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class HashMapAndTreeMap {
	public static void main(String[] args) {
		Map<String, Integer> map = new HashMap<>();
		map.put("banana", 1);
		map.put("apple", 3);
		map.put("cherry", 5);
		map.keySet().forEach(System.out::println);

		Map<String, Integer> treemap = new TreeMap<>();
		treemap.put("banana", 1);
		treemap.put("apple", 3);
		treemap.put("cherry", 5);
		treemap.keySet().forEach(System.out::println);
	}
}
