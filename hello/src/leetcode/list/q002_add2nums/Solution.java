package leetcode.list.q002_add2nums;

/**
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 * 
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single
 * digit. Add the two numbers and return it as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * Example:
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 * 
 * Runtime: 1 ms, faster than 99.99% of Java online submissions for Add Two Numbers.
 * Memory Usage: 43.7 MB, less than 87.15% of Java online submissions for Add Two Numbers.
 * 
 * Faster than solution because the remain list when addition finished is not iterated.
 * 
 * @author ody
 */
public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int c = 0;
		ListNode h1 = l1;
		ListNode r1 = null;
		while (l2 != null && l1 != null) {
			l1.val += l2.val + c;
			c = l1.val / 10;
			l1.val %= 10;
			
			r1 = l1;
			l1 = l1.next;
			l2 = l2.next;
		}
		
		if (l1 == null && r1 != null) {
			r1.next = l2;
			l1 = l2;
		}
		
		while (l1 != null && c > 0) {
			l1.val += c;
			c = l1.val / 10;
			l1.val %= 10;

			r1 = l1;
			l1 = l1.next;
		}
		
		if (c != 0)
			r1.next = new ListNode(c);

		return h1;
	}
}
