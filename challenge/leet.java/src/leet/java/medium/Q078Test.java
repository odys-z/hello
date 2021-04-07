package leet.java.medium;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class Q078Test {

	@SuppressWarnings("serial")
	@Test
	void testSubsets() {
        Q078 q = new Q078();
        int[] nums = new int[] {1, 2, 3};
		List<List<Integer>> r = q.subsets(nums);
		assertTrue(r.size() == 8 && r.containsAll(new ArrayList<List<Integer>>() {
			{ Arrays.asList();
			  Arrays.asList(1);
			  Arrays.asList(2);
			  Arrays.asList(3);
			  Arrays.asList(1, 2);
			  Arrays.asList(1, 3);
			  Arrays.asList(2, 3);
			  Arrays.asList(1, 2, 3);
			}
		}));
	}

}
