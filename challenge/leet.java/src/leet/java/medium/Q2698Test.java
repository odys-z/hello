package leet.java.medium;

import static org.junit.Assert.assertEquals;

import org.junit.jupiter.api.Test;

class Q2698Test {

	@Test
	void test() {
        Q2698 q = new Q2698();
		assertEquals(182, q.punishmentNumber(10));
		assertEquals(1478, q.punishmentNumber(37));
		assertEquals(6528, q.punishmentNumber(66));
		
		System.out.println("Ok !");
	}

}
