package Week10.suhyun.tvpractice;

import java.util.regex.Pattern;

public class Main01 {

	public int solution(String[] emails) {
		// 이메일 정규표현식 패턴
		Pattern pattern = Pattern.compile("^[a-z.]+@[a-z]+\\.(com|net|org)$");
		int count = 0;

		for (String email : emails) {
			if (pattern.matcher(email).matches()) {
				count++;
			}
		}

		return count;
	}

	public static void main(String[] args) {
		Main01 validator = new Main01();
		String[] emails = {"d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"};
		System.out.println(validator.solution(emails));
	}
}
