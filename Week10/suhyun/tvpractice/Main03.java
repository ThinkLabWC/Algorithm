package Week10.suhyun.tvpractice;

import java.util.Arrays;

public class Main03 {

	public static int solution(int money, int[] costs){
		int[] unit = {1, 5, 10, 50, 100, 500};
		int[] dp = new int[money + 1];
		for(int i=1; i<=money; i++){
			dp[i] = Integer.MAX_VALUE;
		}
		dp[0] = 0;
		for(int i=1; i<=money; i++){
			// System.out.println("i = " + i + " " + Arrays.toString(dp));
			for(int j=0; j<unit.length; j++){
				int coin = unit[j]; // 1, 1, 5,
				int cost = costs[j]; // 1, 1, 4
				// dp[i - coin] != Integer.MAX_VALUE 무슨 의미지?
				if(i >= coin && dp[i - coin] != Integer.MAX_VALUE){
					dp[i] = Math.min(dp[i], dp[i - coin] + cost);
				}
			}
		}
		return dp[money];
	}
	// 7원을 만들고 싶다?
	// 1원짜리 7개 => 7
	// 5원짜리 1개, 1원짜리 2개 => 4 + 2 = 6

	public static void main(String[] args) {
		int money = 4578;
		int[] costs = {1, 4, 99, 35, 50, 1000};
		solution(money, costs);
	}
}
