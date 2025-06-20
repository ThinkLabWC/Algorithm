package Week10.suhyun.tvpractice;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class StreamPra02 {
	public static void main(String[] args) {
		Object[] array = {30, "Re_Go", 1, false, 60, "re_go", "st"};
		List<Object> list = Arrays.asList(array);
		// System.out.println(list);

		List<String> mappedList = list.stream()
			.filter(element -> element instanceof String)
			.map(String.class::cast)
			.toList();
		System.out.println(mappedList);

		List<Integer> mappedIntegerList = list.stream()
			.filter(element -> element instanceof Integer)
			.map(Integer.class::cast)
			.toList();
		System.out.println(mappedIntegerList);

		List<Integer> mappedIntegerSortedList = list.stream()
			.filter(element -> element instanceof Integer)
			.map(Integer.class::cast)
			.sorted()
			.toList();
		System.out.println(mappedIntegerSortedList);

		Map<Integer, List<String>> mappedStringGrouping = list.stream()
			.filter(element -> element instanceof String)
			.map(String.class::cast)
			.collect(Collectors.groupingBy(String::length));
		System.out.println(mappedStringGrouping);
	}
}
