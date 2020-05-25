#include <solution.h>


int main()
{
    Solution* s = new Solution();
    int a[] = {1, 2};
    int b[] = {2, 1};
    ListNode* h = Singlist::build(2, a);
    assert(Singlist::eq(2, b, s->swapPairs(h)));

    int c[] = {1, 2, 3, 4};
    int d[] = {2, 1, 4, 3};
    h = Singlist::build(4, c);
    assert(Singlist::eq(2, d, s->swapPairs(h)));
    return 0;
}
