package Week10.suhyun.tvpractice;

import java.text.DecimalFormat;

public class example {
	public static void main(String[] args) {
		int number = 10000000;
		DecimalFormat format = new DecimalFormat("#,###");
		String formatter = format.format(number);
		System.out.println(formatter);
	}
}
