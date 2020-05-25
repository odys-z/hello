#include "singlist.h"

Singlist::Singlist()
{
}

ListNode* Singlist::build (int c, int v[]) {
    ListNode* h = NULL;
    for (int x = c - 1; x >= 0; x--) {
        h = new ListNode(v[x], h);
    }
    return h;
}

bool Singlist::eq (int alen, int a[], ListNode* b) {
    int ax = 0;
    while (ax < alen && b != NULL) {
        if (b == NULL || a[ax] != b->val)
            return false;
        b = b->next;
        ax++;
    }
    if (ax < alen || b != NULL)
        return false;
    if (ax >= alen && b == NULL)
        return false;
    return true;
}
