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
 * @author ody
 */
public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		int c = 0;
		ListNode h1 = l1;
		ListNode r1 = null;
		ListNode r2 = null;
		while (l2 != null && l1 != null) {
			l1.val += l2.val + c;
			c = l1.val / 10;
			l1.val %= 10;
			
			r1 = l1;
			l1 = l1.next;
			r2 = l2;
			l2 = l2.next;
		}
		
		if (l1 == null && r1 != null) {
			r1.next = l2;
			l1 = l2;
		}
		
		while (l1 != null) {
			l1.val += c;
			c = l1.val / 10;
			l1.val %= 10;
			l1 = l1.next;
		}
			
		return h1;
	}
}
