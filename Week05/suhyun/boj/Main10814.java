package Week05.suhyun.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main10814 {

	static class Person implements Comparable<Person>{
		int age;
		String name;
		int f;

		public Person(int age, String name, int f){
			this.age = age;
			this.name = name;
			this.f = f;
		}

		public int compareTo(Person p){
			if(this.age == p.age){
				return this.f - p.f;
			}
			return this.age - p.age;
		}

		public String toString(){
			return age + " " + name;
		}
	}
	static int n;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		List<Person> lists = new ArrayList<>();
		for(int i=0; i<n; i++){
			String[] st = br.readLine().split(" ");
			int age = Integer.parseInt(st[0]);
			String name = st[1];
			lists.add(new Person(age, name, i));
		}
		Collections.sort(lists);
		for(int i=0; i<lists.size(); i++){
			System.out.println(lists.get(i).toString());
		}
	}
}
