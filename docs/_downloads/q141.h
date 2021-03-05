#ifndef Q141_H
#define Q141_H

#include <stdlib.h>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/** 44.02%
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *tortoise = head;
        ListNode *hare = head;

        while (tortoise != NULL and hare != NULL && hare->next != NULL) {
            tortoise = tortoise->next;
            hare = hare->next->next;

            if (tortoise == hare) return true;
        }
        return false;

    }
};

#endif // Q141_H
