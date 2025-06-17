package Week10.suhyun.tvpractice;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class StreamPrac03 {
	public static void main(String[] args) {
		Object[] arr = {"neo", "kakao", "toss", "seo", 15, 1, 6};
		// 1. 배열을 ArrayList로 변환
		List<Object> wrappedArr = Arrays.asList(arr);

		// 2. 맵핑 (Mapping): 문자열인 요소만 추출
		List<String> wrappedString = wrappedArr.stream()
			.filter(element -> element instanceof String)
			.map(String.class::cast)
			.toList();
		System.out.println(wrappedString);

		// 3. 필터링 (Filtering): 숫자인 요소만 추출
		List<Integer> wrappedInteger = wrappedArr.stream()
			.filter(element -> element instanceof Integer)
			.map(Integer.class::cast)
			.toList();
		System.out.println(wrappedInteger);

		// 4. 정렬 (Sorting): 숫자를 오름차순으로 정렬
		List<Integer> wrappedIntegerSorted = wrappedArr.stream()
			.filter(element -> element instanceof Integer)
			.map(Integer.class::cast)
			.sorted()
			.toList();
		System.out.println(wrappedIntegerSorted);

		// 5. 그룹화 (Grouping): 문자열 요소를 길이에 따라 그룹화
		Map<Integer, List<String>> wrappedIntegerGroup = wrappedArr.stream()
			.filter(element -> element instanceof String)
			.map(String.class::cast)
			.collect(Collectors.groupingBy(String::length));
		System.out.println(wrappedIntegerGroup);
	}
}
