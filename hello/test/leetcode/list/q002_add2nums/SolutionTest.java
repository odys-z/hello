package leetcode.list.q002_add2nums;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class SolutionTest {

	private static Solution s;

	@BeforeEach
	void setUp() throws Exception {
		s = new Solution();
	}

	@Test
	void testAddTwoNumbers() {
		assertEqual("", "", "");
		assertEqual("1", "1", "");
		assertEqual("0", "0", "0");
		assertEqual("1", "0", "1");
		assertEqual("2", "1", "1");
		assertEqual("2", "1", "1");
		assertEqual("9", "0", "9");
		assertEqual("10", "9", "1");
		assertEqual("20", "19", "1");
		assertEqual("20000", "19999", "1");
		assertEqual("807", "342", "465");
	}

	static void assertEqual(String expect, String n1, String n2) {
		ListNode l2 = s.addTwoNumbers(toList(n1), toList(n2));
		ListNode l1 = toList(expect);
		while (l1 != null && l2 != null) {
			assertEquals(l1.val, l2.val);
			l1 = l1.next;
			l2 = l2.next;
		}
		assertNull(l1);
		assertNull(l2);
	}
	
	static ListNode toList(String s) {
		if (s != null && s.length() > 0) {
			ListNode p = new ListNode(s.charAt(s.length() - 1) - '0');
			ListNode head = p;
			for (int i = s.length() - 2; i >= 0; i--) {
				ListNode n = new ListNode(s.charAt(i) - '0');
				p.next = n;
				p = n;
			}
			return head;
		}
		return null;
	}
}
