package Week06.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main15904 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		Queue<Character> ucpc = new LinkedList<>();
		ucpc.add('U');
		ucpc.add('C');
		ucpc.add('P');
		ucpc.add('C');
		for(int i=0; i<str.length(); i++){
			if(!ucpc.isEmpty()){
				if(str.charAt(i) == ucpc.peek()){
					ucpc.poll();
				}
			} else {
				break;
			}
		}
		if(ucpc.isEmpty()){
			System.out.println("I love UCPC");
		} else {
			System.out.println("I hate UCPC");
		}
	}
}
