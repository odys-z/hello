package leetcode;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class Q957Test {

	@BeforeEach
	void setUp() throws Exception {
	}

	@Test
	void testPrisonAfterNDays() {
		Q957 s = new Q957();
		int[] cells =     new int[] {0,1,0,1,1,0,0,1};
//		assertArrayEquals(new int[] {1,0,0,1,1,1,1,0},
//				s.prisonAfterNDays(cells , 1));

		cells = new int[] {0,1,0,1,1,0,0,1};
		assertArrayEquals(new int[] {0,0,1,1,0,0,0,0},
				s.prisonAfterNDays(cells , 7));
	}

}
