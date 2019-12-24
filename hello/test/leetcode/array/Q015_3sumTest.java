package leetcode.array;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class Q015_3sumTest {

	@Test
	void testThreeSum() {
		Q015_3sum s = new Q015_3sum();
		List<List<Integer>> lst = s.threeSum2(new int[] {-1, 0, 0, 1});
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(0));

		lst = s.threeSum2(new int[] {-1, 0, 0, 1, 2, 3, -2});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-2, -1, 3), lst.get(0));
		assertEquals(Arrays.asList(-2, 0, 2), lst.get(1));
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(2));
	}

}
