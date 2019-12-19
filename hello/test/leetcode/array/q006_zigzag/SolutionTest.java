package leetcode.array.q006_zigzag;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SolutionTest {

	@Test
	void testConvert() {
		Solution s = new Solution();
		assertEquals("12", s.convert("12", 4));
		assertEquals("1", s.convert("1", 1));
		assertEquals("", s.convert("", 1));
		assertEquals("ABCDEFGHIJKLMNOPQRSTUVW", s.convert("ABCDEFGHIJKLMNOPQRSTUVW", 1));
		assertEquals("PINALSIGYAHRPI", s.convert("PAYPALISHIRING", 4));
		assertEquals("PAHNAPLSIIGYIR", s.convert("PAYPALISHIRING", 3));
		assertEquals("PINALSIGYAHRPI", s.convert("PAYPALISHIRING", 4));
		/*P      H
		 *A   S  I
		 *Y   I  R
		 *P L    I G
		 *A      N
		 *
		 *"PHASIYIRPLIGAN"
		 */
		assertEquals("PHASIYIRPLIGAN", s.convert("PAYPALISHIRING", 5));
		assertEquals("AHBHGACGFBDFECED", s.convert("ABCDEFGHHGFEDCBA", 5));
		assertEquals("ABACBDCEDFEGFHGH", s.convert("ABCDEFGHHGFEDCBA", 9));
	}

}
