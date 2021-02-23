package leet.java.medium;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class Q784Test {

	@Test
	void test() {
        Q784 q = new Q784();
		List<String> r = q.letterCasePermutation("a1b2");
		assertTrue(r.size() == 4 && r.containsAll(Arrays.asList("a1b2", "a1B2", "A1b2", "A1B2")));
		
		r = q.letterCasePermutation("1");
		assertTrue(r.size() == 1 && r.containsAll(Arrays.asList("1")));

		r = q.letterCasePermutation("a");
		assertTrue(r.size() == 2 && r.containsAll(Arrays.asList("a", "A")));

		System.out.println("Ok !");
	}

}
