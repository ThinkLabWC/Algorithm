package Week10.suhyun.tvpractice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class Main02 {

	public long solution(int[] abilities, int k){
		PriorityQueue<Long> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

		for(int ability : abilities){
			priorityQueue.offer((long)ability);
		}

		int totalRounds = (abilities.length + 1) / 2;
		List<Long> differences = new ArrayList<>();
		long answer = 0;

		for(int i=0; i<totalRounds; i++){
			if(priorityQueue.isEmpty()){
				break;
			}

			long first = priorityQueue.poll();
			long second = 0;
			if(!priorityQueue.isEmpty()){
				second = priorityQueue.poll();
			}

			differences.add(first - second);

			answer += second;
		}

		Collections.sort(differences, Collections.reverseOrder());

		for(int i=0; i<Math.min(k, differences.size()); i++){
			answer += differences.get(i);
		}

		return answer;

	}

	public static void main(String[] args) {
		Main02 main02 = new Main02();
		int[] abilities = {9, 8, 6, 3, 2, 1, 1};
		int k = 2;
		long total = main02.solution(abilities, k);
		System.out.println(total);
	}
}
