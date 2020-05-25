#include <solution.h>


int main()
{
    Solution* s = new Solution();
    int r[] = {1};
    int t[] = {1};
    ListNode* h = Singlist::build(1, r);
    assert(Singlist::eq(1, t, s->swapPairs(h)));

    int a[] = {1, 2};
    int b[] = {2, 1};
    h = Singlist::build(2, a);
    assert(Singlist::eq(2, b, s->swapPairs(h)));

    int x[] = {1, 2, 3};
    int y[] = {2, 1, 3};
    h = Singlist::build(3, x);
    assert(Singlist::eq(3, y, s->swapPairs(h)));

    int c[] = {1, 2, 3, 4};
    int d[] = {2, 1, 4, 3};
    h = Singlist::build(4, c);
    assert(Singlist::eq(4, d, s->swapPairs(h)));
    return 0;
}
