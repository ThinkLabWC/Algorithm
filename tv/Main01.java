package tv;

import java.util.regex.Pattern;

public class Main01 {
    public int solution(String[] emails) {
        Pattern pattern = Pattern.compile("^[a-z.]+@[a-z]+\\.(com|net|org)$");
        int count = 0;

        for (String email : emails) {
            if (pattern.matcher(email).matches()) {
                count++;
            }
        }

        return count;
    }

    // 테스트용 main 메서드
    public static void main(String[] args) {
        Main01 sol = new Main01();
        String[] emails = {"d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"};
        System.out.println(sol.solution(emails)); // 출력: 3
    }
}
