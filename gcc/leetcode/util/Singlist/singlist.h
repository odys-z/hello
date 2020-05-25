#ifndef SINGLIST_H
#define SINGLIST_H

#include "Singlist_global.h"

 struct SINGLIST_EXPORT ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}

 };

class SINGLIST_EXPORT Singlist
{
public:
    Singlist();
    static bool eq(int alen, int a[], ListNode* b);
    static ListNode* build(int c, int v[]);
};

#endif // SINGLIST_H
