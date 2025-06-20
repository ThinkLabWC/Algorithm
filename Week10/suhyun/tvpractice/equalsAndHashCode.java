package Week10.suhyun.tvpractice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.stream.LongStream;

public class equalsAndHashCode {
	static class Card implements Comparable<Card>{
		String name;
		String number;
		int a;

		public Card(String name, String number, int a){
			this.name = name;
			this.number = number;
			this.a = a;
		}

		@Override
		public String toString() {
			return "Card{" +
				"name='" + name + '\'' +
				", number='" + number + '\'' +
				", a=" + a +
				'}';
		}

		@Override
		public boolean equals(Object o) {
			if (o == null || getClass() != o.getClass())
				return false;
			Card card = (Card)o;
			return Objects.equals(name, card.name) && Objects.equals(number, card.number);
		}

		@Override
		public int hashCode() {
			return Objects.hash(name, number);
		}

		@Override
		public int compareTo(Card o) {
			return this.a - o.a;
		}
	}

	public static void main(String[] args){
		makeSet();
	}

	public static void makeSet(){
		// Set<Card> cardSet = new HashSet<>();
		// cardSet.add(new Card("Hyundai","0000-0000-0000"));
		// cardSet.add(new Card("Hyundai","0000-0000-0000"));
		//
		// Card card1 = new Card("Hyundai","0000-0000-0000");
		// Card card2 = new Card("Hyundai","0000-0000-0000");
		// System.out.println(card1.equals(card2));
		//
		// cardSet.forEach(System.out::println);
		// System.out.println(cardSet.size());
		Map<Card, Integer> cardIntegerMap = new HashMap<>();
		cardIntegerMap.put(new Card("Hyundai","0000-0000-0000", 1), 1);
		System.out.println(cardIntegerMap.get(new Card("Hyundai","0000-0000-0000", 2)));
		// System.out.println(cardIntegerMap.get(new Card("Hyundai","0000-0000-0000")).toString());
		Card card1 = new Card("Hyundai","0000-0000-0000", 3);
		Card card2 = new Card("Hyundai","0000-0000-0000", 1);
		List<Card> cardList = new ArrayList<>();
		cardList.add(card1);
		cardList.add(card2);
		Collections.sort(cardList);
		System.out.println(cardList);
		System.out.println(card1.toString());
	}
}
