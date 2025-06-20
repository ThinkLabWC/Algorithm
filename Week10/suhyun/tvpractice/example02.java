package Week10.suhyun.tvpractice;

import java.text.DecimalFormat;

public class example02 {
	public static void main(String[] args) {
		int number = 1000;
		DecimalFormat decimalFormat = new DecimalFormat("#,###");
		String formatter = decimalFormat.format(number);
		System.out.println(formatter);
	}
}
