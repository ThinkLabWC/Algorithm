
/* package 구문을 넣으면 안됩니다 */
import java.util.*;
import java.io.*;

/* [Notice for Java]
 * - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
 * - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
 * 
 * - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요 
 * - 입출력의 양이 많은 문제는 BufferedReader와 BufferedWriter를 사용하면 시간을 단축할 수 있습니다.
 * - 클래스 이름은 항상 Main이어야 합니다. 주의하세요.
 * - 모든 입력과 출력은 System.in과 System.out 스트림을 이용해야 합니다.
 */

public class Main {
  static int N, M;
  static String pattern;
  static String[] words;
  static boolean[] visited;
  static String answer = null;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    pattern = br.readLine().trim();
    words = new String[M];

    for (int i = 0; i < M; i++) {
      words[i] = br.readLine().trim();
    }

    Arrays.sort(words); // 사전순 우선

    visited = new boolean[M];
    dfs(0, new StringBuilder());

    System.out.println("결과");
    System.out.println(answer != null ? answer : "");
  }

  static void dfs(int pos, StringBuilder sb) {
    if (answer != null)
      return;
    if (pos > M)
      return;

    String formed = sb.toString();
    if (hasNoQuestion(formed, pattern)) {
      answer = formed + pattern.substring(formed.length());
      return;
    }

    boolean find = false;
    for (int i = 0; i < M; i++) {
      if (visited[i])
        continue;

      String word = words[i];
      int len = word.length();
      if (pos + len > N)
        continue;

      if (canMatch(pattern, pos, word)) {
        find = true;
        visited[i] = true;
        sb.append(word);
        dfs(pos + len, sb);
        sb.setLength(sb.length() - len);
        visited[i] = false;
      }
    }
    if (!find && answer == null) {
      dfs(pos + 1, sb);
    }
  }

  static boolean canMatch(String pattern, int pos, String word) {
    for (int i = 0; i < word.length(); i++) {
      if (pos + i >= pattern.length())
        return false;
      char pc = pattern.charAt(pos + i);
      if (pc != '?' && pc != word.charAt(i)) {
        return false;
      }
    }
    return true;
  }

  static boolean hasNoQuestion(String formed, String pattern) {
    int len = formed.length();
    for (int i = 0; i < len; i++) {
      if (pattern.charAt(i) != '?' && pattern.charAt(i) != formed.charAt(i)) {
        return false;
      }
    }
    // 이후에 ?가 하나라도 있으면 아직 확정된 답이 아님
    for (int i = len; i < pattern.length(); i++) {
      if (pattern.charAt(i) == '?')
        return false;
    }
    return true;
  }
}
