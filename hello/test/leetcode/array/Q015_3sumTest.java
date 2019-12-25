package leetcode.array;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class Q015_3sumTest {
	@Test
	void testThreeSum2() {
		Q015_3sum s = new Q015_3sum();
		List<List<Integer>> lst = null;

		lst = s.threeSum2(new int[] {0, 0, 0});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(0, 0, 0), lst.get(0));

		lst = s.threeSum2(new int[] {-1, 0, 1, 2, -1, -4});
		assertEquals(2, lst.size());
		assertEquals(Arrays.asList(-1, -1, 2), lst.get(0));
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(1));

		lst = s.threeSum2(new int[] {-10, -1, 0, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-10, 2, 8), lst.get(0));
		assertEquals(Arrays.asList(-10, 3, 7), lst.get(1));
		assertEquals(Arrays.asList(-10, 4, 6), lst.get(2));

		lst = s.threeSum2(new int[] {-30, -1, 0, 2, 2, 3, 3, 4, 26, 27, 28, 29});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-30, 2, 28), lst.get(0));
		assertEquals(Arrays.asList(-30, 3, 27), lst.get(1));
		assertEquals(Arrays.asList(-30, 4, 26), lst.get(2));

		lst = s.threeSum2(new int[] {-1, 0, 0, 1});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(0));

		lst = s.threeSum2(new int[] {-1, 0, 0, 1, 2, 3, -2});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-2, -1, 3), lst.get(0));
		assertEquals(Arrays.asList(-2, 0, 2), lst.get(1));
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(2));

		lst = s.threeSum2(new int[] {-1, 0, 0, 0, 0, 0, 0});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(0, 0, 0), lst.get(0));
	}

	@Test
	void testThreeSum3() {
		Q015_3sum s = new Q015_3sum();
		List<List<Integer>> lst = null;

		lst = s.threeSum3(new int[] {0, 0, 0});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(0, 0, 0), lst.get(0));

		lst = s.threeSum3(new int[] {-1, 0, 1, 2, -1, -4});
		assertEquals(2, lst.size());
		assertEquals(Arrays.asList(-1, -1, 2), lst.get(1));
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(0));

		lst = s.threeSum3(new int[] {-10, -1, 0, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-10, 2, 8), lst.get(2));
		assertEquals(Arrays.asList(-10, 3, 7), lst.get(1));
		assertEquals(Arrays.asList(-10, 4, 6), lst.get(0));

		lst = s.threeSum3(new int[] {-30, -1, 0, 2, 2, 3, 3, 4, 26, 27, 28, 29});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-30, 2, 28), lst.get(2));
		assertEquals(Arrays.asList(-30, 3, 27), lst.get(1));
		assertEquals(Arrays.asList(-30, 4, 26), lst.get(0));

		lst = s.threeSum3(new int[] {-1, 0, 0, 1});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(0));

		lst = s.threeSum3(new int[] {-1, 0, 0, 1, 2, 3, -2});
		assertEquals(3, lst.size());
		assertEquals(Arrays.asList(-2, -1, 3), lst.get(2));
		assertEquals(Arrays.asList(-2, 0, 2), lst.get(1));
		assertEquals(Arrays.asList(-1, 0, 1), lst.get(0));

		lst = s.threeSum3(new int[] {-1, 0, 0, 0, 0, 0, 0});
		assertEquals(1, lst.size());
		assertEquals(Arrays.asList(0, 0, 0), lst.get(0));
	}

}
