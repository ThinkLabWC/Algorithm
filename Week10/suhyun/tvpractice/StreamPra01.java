package Week10.suhyun.tvpractice;

import java.io.LineNumberInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class StreamPra01 {
	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5};
		IntStream intStream = Arrays.stream(arr);
		Integer[] arrWrapper = {1, 2, 3, 4, 5};
		Stream<Integer> arrWrraperStream = Arrays.stream(arrWrapper);
		int sum = intStream.sum();
		System.out.println(sum);
		int wrraperSum = arrWrraperStream.mapToInt(Integer::intValue).sum();
		System.out.println(wrraperSum);
	}
}
