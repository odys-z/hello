#ifndef SOLUTION_H
#define SOLUTION_H


#include "singlist.h"

/**
 * @brief The Solution class
 * https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
 *
 * Given a linked list, swap every two adjacent nodes and return its head.
 * You may not modify the values in the list's nodes, only nodes itself may be changed.
 */
class Solution
{
public:
    Solution() {};
    ~Solution() {};

    /**
     * Runtime: 0 ms, faster than 100.00% of C++ online submissions for Swap Nodes in Pairs.
     * Memory Usage: 7.6 MB, less than 100.00% of C++ online submissions for Swap Nodes in Pairs.
     *
     * @brief swapPairs
     * @param head
     * @return
     */
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL)
            return head;
        else if (head->next == NULL)
            return head;

        ListNode* _h = NULL;
        ListNode* h = head;
        ListNode* h_ = head->next;
        head = h_;

        while (h != NULL && h_ != NULL) {
            // swap h, h_
            h->next = h_->next;
            h_->next = h;

            // step _h
            if (_h != NULL)
                _h->next = h_;
            _h = h;

            // step: h_, h -> next h, h_
            h = h == NULL ? NULL : h->next;
            h_ = h == NULL ? NULL : h->next;
        }
        return head;
    }

};

#endif // SOLUTION_H
