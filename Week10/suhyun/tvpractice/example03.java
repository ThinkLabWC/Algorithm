package Week10.suhyun.tvpractice;

import java.text.DecimalFormat;
import java.util.function.IntFunction;

public class example03 {
	public static void main(String[] args) {
		int num = 100000;
		DecimalFormat decimalFormat = new DecimalFormat("#,###");
		String s = decimalFormat.format(num);
		System.out.println(s);

		IntFunction intFunction = (x) -> x + 1;
		System.out.println(intFunction.apply(1));
	}
}
