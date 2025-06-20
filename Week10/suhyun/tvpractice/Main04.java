package Week10.suhyun.tvpractice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main04 {
	public static int[] solution(int num_teams, String[] remote_tasks, String[] office_tasks, String[] employees){
		Set<String> remoteTasks = new HashSet<>(Arrays.asList(remote_tasks));
		Set<String> officeTasks = new HashSet<>(Arrays.asList(office_tasks));

		// 팀별 직원목록 관리
		Map<Integer, List<Integer>> teamEmployees = new HashMap<>();
		// 재택가능한 직원 목록
		Set<Integer> remoteWorkCandidates = new HashSet<>();

		// employees의 원소는 "team_number task_list"형태의 문자열
		// team_number는 해당 사원의 팀 번호, task_list는 해당 사원의 담당 업무를 나타내는 문자열
		for(int i=0; i<employees.length; i++){
			String[] info = employees[i].split(" ");
			int teamNo = Integer.parseInt(info[0]);
			teamEmployees.computeIfAbsent(teamNo, k -> new ArrayList<>()).add(i + 1);
			// {1:[1,2], 2:[3,4]}

			boolean canWorkRemote = true;
			for(int j=1; j<info.length; j++){
				if(officeTasks.contains(info[j])){
					canWorkRemote = false;
					break;
				}
			}

			// 만약 재택근무 대상자라면,
			if(canWorkRemote){
				remoteWorkCandidates.add(i + 1);
			}
		}

		// 팀별로 확인, 팀별로
		for(List<Integer> teamMembers : teamEmployees.values()){
			boolean allRemote = true;
			for(int i : teamMembers){
				if(!remoteWorkCandidates.contains(i)){
					allRemote = false;
					break;
				}
			}

			// 2번팀이 3번, 4번 사원이 존재
			if(allRemote){
				remoteWorkCandidates.remove(Collections.min(teamMembers));
			}
		}

		return remoteWorkCandidates.stream()
			.mapToInt(Integer::intValue)
			.sorted()
			.toArray();
	}

	public static void main(String[] args) {
		int num_teams = 3;
		String[] remote_tasks = {"development", "marketing", "hometask"};
		String[] office_tasks = {"a", "b", "c"};
		String[] employees = {
			"1 development hometask",
			"1 a marketing",
			"2 hometask",
			"2 development marketing hometask",
			"3 marketing",
			"3 c",
			"3 development"
		};

		int[] result = solution(num_teams, remote_tasks, office_tasks, employees);

		System.out.println("재택 근무 사원 번호: " + Arrays.toString(result));
	}
}
