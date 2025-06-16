package Week10.suhyun.tvpractice;

import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class equalsAndHashCode {
	static class Card{
		String name;
		String number;

		public Card(String name, String number){
			this.name = name;
			this.number = number;
		}

		@Override
		public String toString() {
			return "Card{" +
				"name='" + name + '\'' +
				", number='" + number + '\'' +
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
	}

	public static void main(String[] args){
		makeSet();
	}

	public static void makeSet(){
		Set<Card> cardSet = new HashSet<>();
		cardSet.add(new Card("Hyundai","0000-0000-0000"));
		cardSet.add(new Card("Hyundai","0000-0000-0000"));

		Card card1 = new Card("Hyundai","0000-0000-0000");
		Card card2 = new Card("Hyundai","0000-0000-0000");
		System.out.println(card1.equals(card2));

		cardSet.forEach(System.out::println);
		System.out.println(cardSet.size());
	}
}
