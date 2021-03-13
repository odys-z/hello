package leet.java.medium;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Q1130Test {

	@Test
	void test() {
		Q1130 q = new Q1130();
		assertEquals(32, q.mctFromLeafValues(new int[] {6, 2, 4}));
		assertEquals(315, q.mctFromLeafValues(new int[] {6,1,5,5,5,5,5,15,6}));
		
		System.out.println("Ok !");
	}

}
