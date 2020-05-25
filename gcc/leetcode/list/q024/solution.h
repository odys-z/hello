#ifndef SOLUTION_H
#define SOLUTION_H


#include "singlist.h"

class Solution
{
public:
    Solution() {};
    ~Solution() {};

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
